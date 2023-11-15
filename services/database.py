import json

max_id = None


class Database(object):
    def __init__(self):
        self.json_file_path = "db.json"
        self.data = self.load_data()

    def load_data(self):
        global max_id

        try:
            with open(self.json_file_path, 'r') as file:
                res = []
                data = json.load(file)
                for d in data:
                    res.append(json.loads(d) if isinstance(d, str) else d)

            max_id = 0 if len(res) == 0 else max(res, key=lambda x: x['id'])['id']

            return res
        except FileNotFoundError:
            # If the file doesn't exist, create an empty data structure
            max_id = 0
            return []

    def save_data(self):
        with open(self.json_file_path, 'w') as file:
            res = []
            for d in self.data:
                if hasattr(d, 'json') and callable(d.json):
                    res.append(d.json())
                else:
                    res.append(d)

            json.dump(res, file, indent=2)

    def insert_data(self, record):
        self.data.append(record)
        self.save_data()

    def get_all_data(self):
        return self.data

    def delete_data(self, record_id):
        removed = None
        new_data = []

        for record in self.data:
            if record.get('id') != record_id:
                new_data.append(record)
            else:
                removed = record

        self.data = new_data
        self.save_data()
        return removed

    def update_data(self, record_id, new_values):
        for record in self.data:
            if record.get('id') == record_id:
                record.update(new_values)
        self.save_data()

    def search_by_criteria(self, search_criteria):
        if 'id' in search_criteria:
            record_id = search_criteria['id']
            return [record for record in self.data if record.get('id') == record_id]
        else:
            return [record for record in self.data if all(record[key] == value for key, value in search_criteria.items())]

    def get_record_by_id(self, record_id):
        results = self.search_data({'id': record_id})
        return results[0] if results else None

    def group_by(self, key):
        grouped_data = {}
        for record in self.data:
            value = record.get(key)
            if value not in grouped_data:
                grouped_data[value] = []
            grouped_data[value].append(record)
        return grouped_data

    def sort_by(self, key, reverse=False):
        self.data.sort(key=lambda x: x.get(key), reverse=reverse)
        return self.data

