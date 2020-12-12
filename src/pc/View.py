from VoltageData import VoltageData
import matplotlib.pyplot as plt


class View:
    def __init__(self, data, top=5.0, bottom=-5.0):
        self.top = top
        self.bottom = bottom
        self.data = data

        self.fig = plt.figure(figsize=(12.8, 7.2))
        self.axes = self._figure_create_axes(self.fig, data.size)

    def _figure_create_axes(self, fig, size):
        if size == 1:
            return [fig.add_subplot(1, 1, 1)]

        if size == 2:
            return [fig.add_subplot(1, 2, 1), fig.add_subplot(1, 2, 2)]

        if size == 3 or size == 4:
            return [fig.add_subplot(2, 2, i + 1) for i in range(size)]

        if size == 5 or size == 6:
            return [fig.add_subplot(2, 3, i + 1) for i in range(size)]

    def _draw(self, ax, data):
        ax.plot(data.time, data.data, label=data.label)
        ax.legend(loc='upper right')
        ax.set_ylim(self.bottom, self.top)
        ax.set_xlabel("time")
        ax.set_ylabel("Voltage (mV)")

    def show(self, sleep_time=0.0001, clear=False):
        for ax, ch_data in zip(self.axes, self.data.data):
            self._draw(ax, ch_data)
        plt.draw()
        plt.pause(sleep_time)

    def update(self, sleep_time=0.0001):
        for ax in self.axes:
            ax.cla()
        self.show(sleep_time)