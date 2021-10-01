import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plot_style import plot_style
import matplotlib.gridspec as gridspec

plt.rcParams.update(plot_style)
plt.style.use('ggplot')
np.random.seed(0)


def plot_error(x_axis, y_axis, model, sample_size):
    for i in range(sample_size):
        plt.plot([x_axis[i], x_axis[i]], [y_axis[i], model[i]], color='salmon', alpha=0.5, linewidth=0.7)


def residual_plot(y_test, y_hat):
    residual = y_test - y_hat
    fig = plt.figure()
    gs = gridspec.GridSpec(1, 2, width_ratios=[2,1])
    plt.subplot(gs[0])
    plt.scatter(y_hat, residual, s=4, color='salmon', alpha=0.7)
    plt.xlabel(r"$Predicted Value$")
    plt.ylabel(r"$Residuals$")
    plt.axhline(0, color='black', linestyle='--', linewidth=0.7, label=r"$C$")

    plt.subplot(gs[1])
    plt.hist(residual, 25, orientation="horizontal", density=True)
    plt.xlabel(r"$Distribution  of  Residuals$")
    fig.suptitle(r"$Residual  Analysis$")


def rss(y_actual, y_predicted):
    return np.sum(np.square(y_actual - y_predicted))


def plot_point(parameter, x, y, label):
    plt.scatter(x[parameter], y[parameter], color='black', s=10)
    plt.annotate(text=label, xy=(x[parameter], y[parameter]), xytext=(x[parameter], y[parameter]+10000))


def plot_rss(x_actual, y_actual, size):
    b = 0
    m = np.linspace(0, 2, size)
    df = pd.DataFrame({'m': m})
    rss_series = np.empty(size)
    rss_series.fill(0)
    fig = plt.figure()
    fig.suptitle(r"\textbf{Hypothesis Space}")
    for i in range(size):
        rss_series[i] = rss(y_actual, m[i] * x_actual + b)
    plt.plot(df['m'], rss_series, color='green', alpha=0.5)
    plot_point(12, m, rss_series, "$A$")
    plot_point(24, m, rss_series, "$B$")
    plot_point(38, m, rss_series, "$C$")
    plt.xlabel(r"$\beta_1{\longrightarrow}$")
    plt.ylabel(r"$RSS{\longrightarrow}$")


def scatter_plot(x, y):
    fig = plt.figure()
    plt.scatter(x, y, s=5, alpha=0.7, color='salmon')
    plt.xlabel(r"$X{\longrightarrow}$")
    plt.ylabel(r"$Y{\longrightarrow}$")
    fig.suptitle(r"\textbf{Scatter plot of $Y$ vs $X$}")


sample_size = 100
X = np.linspace(0, 100, num=sample_size)
y_data = X + np.random.normal(0, 10, sample_size, )

model = np.poly1d(np.polyfit(X, y_data, 1))

y_hat = model(X)
y_null = np.empty(sample_size)
y_null.fill(sample_size/2)

# plot_rss(X, y_data, 50)                           # plot hypothesis space


# plt.plot(X, y_hat, color='orange')                # Linear regression
# plot_Error(X, y_data, y_hat, sample_size)         # plot residuals


# plt.plot(X, y_null, color='royalblue')
# plot_Error(X, y_data, y_null, sample_size)        # Null hypothesis
# plt.plot(X, model(X), color='purple')             # Polunomial regression


# residual_plot(y_data, y_hat)                      # residual analysis and residual distribution
scatter_plot(X, y_data)

plt.show()


