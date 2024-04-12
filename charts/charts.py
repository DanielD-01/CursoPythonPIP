import matplotlib.pyplot as plt

def making_a_pie_chart():
    labels = ["A", "B", "C"]
    values = [22,34,120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()

making_a_pie_chart()