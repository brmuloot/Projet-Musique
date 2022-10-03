from cProfile import label
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import helpers.data_functions as df


def display_something(data, xlabel, table_column ) :

    song_popularity = []
    second_paramater = []
    for row in data:
        second_paramater.append(row[table_column])
        song_popularity.append(row[2])
    root = tkinter.Tk()
    root.wm_title("Etudes graphiques")
    #creer la frame principale
    frame = tkinter.Frame(root, bg='#4065A4')
    frame.pack(expand=tkinter.YES)
    #creer une sous boite
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot()
    ax.scatter(second_paramater,song_popularity)
    ax.set_xlabel(xlabel=xlabel)
    ax.set_ylabel("popularity")
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    pack_toolbar=False #will make it easier to use a layout manager later on.
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    
    toolbar.update()
    canvas.mpl_connect(
        "key_press_event", lambda event: print(f"you pressed {event.key}"))
    canvas.mpl_connect("key_press_event", key_press_handler)
    button_quit = tkinter.Button(master=root, text="Quit", command=root.destroy)
    button_quit.pack(side=tkinter.BOTTOM)
    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

    dropdown = tkinter.Menubutton( root, text = "Choisir en x")
    choice = tkinter.Menu(dropdown, tearoff=0)
    choice.add_command(label="popularity artist", command= lambda:[root.destroy(), display_something(data, 'popu artist', table_column=26)])
    choice.add_command(label="nb de followers", command= lambda:[root.destroy(),display_something(data, 'nb de followers', table_column=23)])
    choice.add_command(label="popularity artist", command= lambda:[root.destroy(), display_something(data, 'popu artist', table_column=21)])
    choice.add_command(label="3", command= lambda:[root.destroy(), display_something(data, 'popu artist', table_column=20)])
    choice.add_command(label="4", command= lambda:[root.destroy(), display_something(data, 'popu artist', table_column=19)])
    choice.add_command(label="5", command= lambda:[root.destroy(), display_something(data, 'popu artist', table_column=17)])
    dropdown["menu"] = choice
    dropdown.pack(side=tkinter.BOTTOM)


    tkinter.mainloop()




def main(): 

    #============Récupération des données ====================

    database = r"C:\Users\utilisateur\Downloads\Ressources\Sources_data.db"
    conn = df.create_connection(database)
    
    #df.associate_data(conn, 5000)  
    data = df.get_everything_from_top_songs(conn,50)
    display_something(data, "followers", 23)  
    
    
    

    # ===================== TKinter INTERFACE ============================


if __name__ == "__main__":
    main()