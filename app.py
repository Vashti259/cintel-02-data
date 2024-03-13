import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins
import seaborn

ui.page_opts(title="Vashti's Unique App", fillable=True)
with ui.layout_columns():
    with ui.sidebar():
        ui.input_slider("n", "N", 25, 50, 200)


@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 25 + 20 * np.random.randn(45)
    plt.hist(x, input.n(), density=True)


from palmerpenguins import load_penguins
from shiny import render
from shiny.express import ui

penguins = load_penguins()
ui.h2("Palmer Penguins")


@render.data_frame
def penguins_df():
    return render.DataGrid(penguins)


@render.plot(alt="A Seaborn histogram on penguin body mass in grams.")
def plot():
    ax = seaborn.histplot(data=penguins, x="body_mass_g", bins=input.n())
    ax.set_title("Palmer Penguins")
    ax.set_xlabel("Mass (g)")
    ax.set_ylabel("Count")
    return ax
