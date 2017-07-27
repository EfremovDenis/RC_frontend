from DB_worker import DB_worker
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab


def plot_for_batch(connection, list_tag_id, batch_id):

    list_tag_names = []
    list_time_stamps = []
    list_values = []

    max_x = float("-inf")
    min_x = float("inf")
    max_y = float("-inf")
    min_y = float("inf")

    for tag_id in list_tag_id:
        tag = DB_worker.select_tag(connection=connection, tag_id=tag_id)
        list_tag_names.append(tag[0][1])

        samples_for_tag = DB_worker.select_samples_tag_batch(connection=connection, tag_id=tag_id, batch_id=batch_id)

        time_stamps = []
        values = []
        for row in samples_for_tag:
            time_stamps.append(row[0])
            values.append(row[1])

        if max(time_stamps) > max_x:
            max_x = max(time_stamps)
        if min(time_stamps) < min_x:
            min_x = min(time_stamps)
        if max(values) > max_y:
            max_y = max(values)
        if min(values) < min_y:
            min_y = min(values)

        list_time_stamps.append(time_stamps)
        list_values.append(values)

    batch = DB_worker.select_batch(connection=connection, batch_id=batch_id)

    plot_init(list_tag_names=list_tag_names, list_time_stamps=list_time_stamps, list_values=list_values,
              max_x=max_x, min_x=min_x, max_y=max_x, min_y=min_y, batch=batch)
    plt.show()
    return


def plot_init(list_tag_names, list_time_stamps, list_values, max_x, min_x, max_y, min_y, batch):

    # These are the "Tableau 20" colors as RGB. # TODO: should be extended ?
    tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
                 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
                 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
                 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
                 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for i in range(len(tableau20)):
        r, g, b = tableau20[i]
        tableau20[i] = (r / 255., g / 255., b / 255.)

    plt.figure(figsize=(14, 12))

    # Remove the plot frame lines.
    ax = plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    plt.ylim(min_y, max_y)
    plt.xlim(min_x, max_x)

    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14)

    tick_step = int(round((max_y - min_y)/10))
    r_min_y = int(round(min_y))
    r_min_x = int(round(min_x))
    r_max_y = int(round(max_y))
    r_max_x = int(round(max_x))

    for y in range(r_min_y, r_max_y, tick_step):
        plt.plot(range(r_min_x, r_max_x), [y] * len(range(r_min_x, r_max_x)), "--", lw=0.5, color="black", alpha=0.3)

    # Remove the tick marks
    plt.tick_params(axis="both", which="both", bottom="off", top="off",
                    labelbottom="on", left="off", right="off", labelleft="on")

    for i in range(0, len(list_tag_names)):

        plt.plot(list_time_stamps[i], list_values[i], lw=2.5, color=tableau20[i])

        y_pos = list_values[i][-1]
        plt.text(max_x, y_pos, list_tag_names[i], fontsize=14, color=tableau20[i])

    params = {'axes.titlesize': 17}
    pylab.rcParams.update(params)
    plt.title(batch[0][3])

    return


# TODO: solve problems with blank export
def save_fig_to_png(full_name):
    plt.savefig("{0}.png".format(full_name), bbox_inches="tight")
    return


def save_fig_to_jpeg(full_name):
    plt.savefig("{0}.jpeg".format(full_name), bbox_inches="tight")
    return


def save_fig_to_svg(full_name):
    plt.savefig("{0}.svg".format(full_name), bbox_inches="tight")
    return


def save_fig_to_pdf(full_name):
    plt.savefig("{0}.pdf".format(full_name), bbox_inches="tight")
    return


def save_fig_to_eps(full_name):
    plt.savefig("{0}.eps".format(full_name), bbox_inches="tight")
    return
