from DataRepresenter import Data_representer
import sqlite3

connection = sqlite3.connect("../measured_data.db")
list_tag_id = [1, 2]
batch_id = 2
Data_representer.plot_for_batch(connection=connection, list_tag_id=list_tag_id, batch_id=batch_id)
Data_representer.save_fig_to_png("C:/test/siski")
