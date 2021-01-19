from notion.client import NotionClient

token = "2ad920952a04d9b424b463cbd5890af0dc2b7864497d5f43bb9c8b083c6612f6c8417747f55bc5899e894950ed59a0a177e45c399a3d21c4b9d44f583105a74c9876fc187827697bf8b7f8631c32"

client = NotionClient(token_v2=token)

tracker_url = "https://www.notion.so/1a357fb6f1254a108fdfaf594d6d46c0?v=bf52b7f77b8d4b7280cf94ad74772fdf"

page = client.get_block(tracker_url)

collection_view = client.get_collection_view(tracker_url)

new_row = collection_view.collection.add_row()


new_row.Tarefa1 = True
new_row.Tags = ("Teste")
new_row.Nome = ("Texto")








