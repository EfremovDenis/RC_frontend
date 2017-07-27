# TODO (to be discussed): GLOBAL TRY CATCH IN ALL FUNCTIONS ???


def select_samples_under_batch(connection, batch_id):
    """
    Selects all samples under one batch.
    Args:
        connection: connection object to the database
        batch_id: the database id of the selected batch
    Returns:
        all samples under the wanted batch id in format (id, tag_id, batch_id, time_stamp, value)
    """

    if not select_batch(connection=connection, batch_id=batch_id):
        TypeError('There is no batch with ID [{0}]'.format(batch_id))

    cursor = connection.cursor()

    format_str = """SELECT * FROM sample
        WHERE batch_id = "{batch_id}"
        ORDER BY tag_id, time_stamp;"""

    select_sample = format_str.format(batch_id=batch_id)

    all_sample_under_batch = []
    for row in cursor.execute(select_sample):
        all_sample_under_batch.append(row)

    connection.commit()

    return all_sample_under_batch


def select_samples_under_tag(connection, tag_id):
    """
    Selects all samples under one tag.
    Args:
        connection: connection object to the database
        tag_id: the database id of the selected tag
    Returns:
        all samples under the wanted tag id in format (id, tag_id, batch_id, time_stamp, value)
    """

    if not select_tag(connection=connection, tag_id=tag_id):
        TypeError('There is no batch with ID [{0}]'.format(tag_id))

    cursor = connection.cursor()

    format_str = """SELECT * FROM sample
        WHERE tag_id = "{tag_id}"
        ORDER BY time_stamp;"""

    select_sample = format_str.format(tag_id=tag_id)

    all_sample_under_tag = []
    for row in cursor.execute(select_sample):
        all_sample_under_tag.append(row)

    connection.commit()

    return all_sample_under_tag


def select_all_batches(connection):
    """
    Selects all batches in the database.
    Args:
        connection: connection object to the database
    Returns:
        List of all batches, which are in format ((id, start_date, stop_date, description)
    """
    cursor = connection.cursor()

    format_str = """SELECT * FROM batch;"""

    all_batches = []
    for row in cursor.execute(format_str):
        all_batches.append(row)

    connection.commit()

    return all_batches


def select_all_tags(connection):
    """
    Selects all tags in the database.
    Args:
        connection: connection object to the database
    Returns:
        List of all tags, which are in format (id, name, from_bit, bit_len, sensor_id)
    """
    cursor = connection.cursor()

    format_str = """SELECT * FROM tag;"""

    all_tags = []
    for row in cursor.execute(format_str):
        all_tags.append(row)

    connection.commit()

    return all_tags


def select_tag_with_sensor_id(connection, sensor_id):
    """
    Selects tag with the defined sensor id.
    Args:
        connection: connection object to the database
        sensor_id: wanted sensor_id
    Returns:
        id of the searched tag OR None in case, when tag with the desired sensor_id does not exist.
    """
    if sensor_id is None:
        raise ValueError('Sensor_id can not be null!')
    if not isinstance(sensor_id, int):
        raise ValueError('Sensor_id must be int!')

    cursor = connection.cursor()

    format_str = """
        SELECT id FROM tag
        WHERE sensor_id = "{sensor_id}";"""

    select_tag_where = format_str.format(sensor_id=sensor_id)

    cursor.execute(select_tag_where)

    list_tag_id = cursor.fetchall()

    # check if list is empty
    if not list_tag_id:
        tag_id = None
    else:
        tag_id = list_tag_id[0][0]

    return tag_id


def select_batch(connection, batch_id):
    """
    Selects batch with batch_id.
    Args:
        connection: connection object to the database
        batch_id: wanted batch_id
    Returns:
        List of the searched batches in format (id, start_date, stop_date, description).
    """
    if batch_id is None:
        raise ValueError('Batch_id can not be null!')
    if not isinstance(batch_id, int):
        raise ValueError('Batch_id must be int!')

    cursor = connection.cursor()

    format_str = """
            SELECT * FROM batch
            WHERE id = "{batch_id}";"""

    select_batch_where = format_str.format(batch_id=batch_id)

    cursor.execute(select_batch_where)

    return cursor.fetchall()


def select_tag(connection, tag_id):
    """
    Selects tag with tag_id.
    Args:
        connection: connection object to the database
        tag_id: wanted tag_id
    Returns:
        List of the searched tags in format (id, name, from_bit, bit_len, sensor_id). !!!!!!!
    """
    if tag_id is None:
        raise ValueError('Tag_id can not be null!')
    if not isinstance(tag_id, int):
        raise ValueError('Tag_id must be int!')

    cursor = connection.cursor()

    format_str = """
            SELECT * FROM tag
            WHERE id = "{tag_id}";"""

    select_tag_where = format_str.format(tag_id=tag_id)

    cursor.execute(select_tag_where)

    return cursor.fetchall()


def select_samples_tag_batch(connection, tag_id, batch_id):
    """
    Selects all samples under one batch and one tag.
    Args:
        connection: connection object to the database
        tag_id: the database id of the selected tag
        batch_id: the database id of the selected batch
    Returns:
        all samples under the wanted batch_id and tag_id in format (time_stamp, value)
    """

    if not select_batch(connection=connection, batch_id=batch_id):
        TypeError('There is no batch with ID [{0}]'.format(batch_id))

    if not select_tag(connection=connection, tag_id=tag_id):
        TypeError('There is no tag with ID [{0}]'.format(tag_id))

    cursor = connection.cursor()

    format_str = """SELECT time_stamp, value FROM sample
            WHERE batch_id = "{batch_id}"
            AND tag_id = "{tag_id}"
            ORDER BY time_stamp;"""

    select_sample = format_str.format(batch_id=batch_id, tag_id=tag_id)

    all_samples = []
    for row in cursor.execute(select_sample):
        all_samples.append(row)

    connection.commit()

    return all_samples
