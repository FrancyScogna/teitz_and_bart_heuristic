import tkinter
import tkinter.messagebox
import webbrowser

from modules import *

class App:
    def __init__(self, root):
        root.title("P-Medians and Clustering solutor by Teitz e Bart Heuristic Algorithm")
        root.iconbitmap('./icon.ico')
        width=1040
        height=650
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_996=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_996["font"] = ft
        GLabel_996["fg"] = "#333333"
        GLabel_996["anchor"] = "w"
        GLabel_996["text"] = "Select json file"
        GLabel_996.place(x=65,y=20,width=301,height=53)

        self.GButton_129=tk.Button(root)
        self.GButton_129["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        self.GButton_129["font"] = ft
        self.GButton_129["fg"] = "#000000"
        self.GButton_129["justify"] = "center"
        self.GButton_129["text"] = "Open"
        self.GButton_129.place(x=85,y=70,width=130,height=35)
        self.GButton_129["command"] = self.GButton_129_command

        self.cities_names = []
        self.cities_coords = {}

        self.GLabel_194=tk.Label(root)
        self.GLabel_194["bg"] = "#ffffff"
        ft = tkFont.Font(family='Times',size=15)
        self.GLabel_194["font"] = ft
        self.GLabel_194["fg"] = "#333333"
        self.GLabel_194["anchor"] = "w"
        self.GLabel_194["text"] = ""
        self.GLabel_194["relief"] = "ridge"
        self.GLabel_194.place(x=230,y=70,width=600,height=35)

        GLabel_924=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_924["font"] = ft
        GLabel_924["fg"] = "#333333"
        GLabel_924["anchor"] = "w"
        GLabel_924["text"] = "Nodes Loaded:"
        GLabel_924.place(x=230,y=110,width=177,height=50)

        self.GLabel_360=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        self.GLabel_360["font"] = ft
        self.GLabel_360["fg"] = "#ff3d00"
        self.GLabel_360["anchor"] = "w"
        self.GLabel_360["text"] = "0"
        self.GLabel_360.place(x=340,y=108,width=163,height=55)
        self.GLabel_360.configure(justify="left")

        GLabel_991=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_991["font"] = ft
        GLabel_991["fg"] = "#333333"
        GLabel_991["anchor"] = "w"
        GLabel_991["text"] = "Insert P Variable"
        GLabel_991.place(x=65,y=150,width=414,height=50)

        self.GLineEdit_296=tk.Entry(root)
        self.GLineEdit_296["bg"] = "#ffffff"
        self.GLineEdit_296["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        self.GLineEdit_296["font"] = ft
        self.GLineEdit_296["fg"] = "#333333"
        self.GLineEdit_296["state"] = "disable"
        self.GLineEdit_296["text"] = ""
        self.GLineEdit_296.place(x=130,y=204,width=80,height=30)

        GLabel_987=tk.Label(root)
        ft = tkFont.Font(family='Times',size=17)
        GLabel_987["font"] = ft
        GLabel_987["fg"] = "#333333"
        GLabel_987["anchor"] = "e"
        GLabel_987["text"] = "P ="
        GLabel_987.place(x=40,y=190,width=83,height=56)

        GLabel_236=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_236["font"] = ft
        GLabel_236["fg"] = "#333333"
        GLabel_236["anchor"] = "w"
        GLabel_236["text"] = "Start heuristic algorithm"
        GLabel_236.place(x=65,y=250,width=404,height=43)

        self.GButton_95=tk.Button(root)
        self.GButton_95["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        self.GButton_95["font"] = ft
        self.GButton_95["fg"] = "#000000"
        self.GButton_95["justify"] = "center"
        self.GButton_95["text"] = "Start"
        self.GButton_95["state"] = "disable"
        self.GButton_95.place(x=85,y=300,width=140,height=35)
        self.GButton_95["command"] = self.GButton_95_command

        self.GButton_200 = tk.Button(root)
        self.GButton_200["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=13)
        self.GButton_200["font"] = ft
        self.GButton_200["fg"] = "#ff0000"
        self.GButton_200["justify"] = "center"
        self.GButton_200["text"] = "Stop"
        self.GButton_200["state"] = "disable"
        self.GButton_200.place(x=240, y=300, width=140, height=35)
        self.GButton_200["command"] = self.GButton_200_command

        GLabel_341=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_341["font"] = ft
        GLabel_341["fg"] = "#ff3d00"
        GLabel_341["anchor"] = "w"
        GLabel_341["text"] = "Best Solution:"
        GLabel_341.place(x=65,y=350,width=268,height=30)

        GLabel_859=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_859["font"] = ft
        GLabel_859["fg"] = "#333333"
        GLabel_859["anchor"] = "w"
        GLabel_859["text"] = "Medians: "
        GLabel_859.place(x=70,y=370,width=145,height=51)

        ScrolMed_x = tk.Scrollbar(root, orient="horizontal")
        ScrolMed_x.place(x=87, y=549, width=290, height=20)
        ScrolMed_y = tk.Scrollbar(root, orient="vertical")
        ScrolMed_y.place(x=376, y=420, width=20, height=130)

        self.GListBox_280=tk.Listbox(root, xscrollcommand=ScrolMed_x.set, yscrollcommand=ScrolMed_y.set)
        self.GListBox_280["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        self.GListBox_280["font"] = ft
        self.GListBox_280["fg"] = "#333333"
        self.GListBox_280["justify"] = "left"
        self.GListBox_280.place(x=87,y=420,width=290,height=130)

        ScrolMed_x["command"] = self.GListBox_280.xview
        ScrolMed_y["command"] = self.GListBox_280.yview

        GLabel_417=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_417["font"] = ft
        GLabel_417["fg"] = "#333333"
        GLabel_417["anchor"] = "w"
        GLabel_417["text"] = "Best Objective:"
        GLabel_417.place(x=70,y=570,width=166,height=42)

        self.Label_119=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        self.Label_119["font"] = ft
        self.Label_119["fg"] = "#333333"
        self.Label_119["anchor"] = "w"
        self.Label_119["text"] = "0.0"
        self.Label_119["fg"] = "#008000"
        self.Label_119.place(x=210,y=571,width=417,height=42)

        ScrolLog_x = tk.Scrollbar(root, orient="horizontal")
        ScrolLog_x.place(x=450,y=529,width=480, height=20)
        ScrolLog_y = tk.Scrollbar(root, orient="vertical")
        ScrolLog_y.place(x=929, y=160, width=20, height=370)

        self.GListBox_26 = tk.Listbox(root, xscrollcommand=ScrolLog_x.set, yscrollcommand=ScrolLog_y.set)
        self.GListBox_26["bg"] = "#ffffff"
        self.GListBox_26["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=13)
        self.GListBox_26["font"] = ft
        self.GListBox_26["fg"] = "#333333"
        self.GListBox_26["justify"] = "left"
        self.GListBox_26["exportselection"] = False
        self.GListBox_26.place(x=450, y=160, width=480, height=370)

        ScrolLog_x["command"] = self.GListBox_26.xview
        ScrolLog_y["command"] = self.GListBox_26.yview

        self.GButton_450=tk.Button(root)
        self.GButton_450["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        self.GButton_450["font"] = ft
        self.GButton_450["fg"] = "#000000"
        self.GButton_450["justify"] = "center"
        self.GButton_450["text"] = "Save Log"
        self.GButton_450["state"] = "disable"
        self.GButton_450.place(x=720,y=560,width=100,height=35)
        self.GButton_450["command"] = self.GButton_450_command

        self.GButton_893=tk.Button(root)
        self.GButton_893["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        self.GButton_893["font"] = ft
        self.GButton_893["fg"] = "#000000"
        self.GButton_893["justify"] = "center"
        self.GButton_893["text"] = "Clusters"
        self.GButton_893["state"] = "disable"
        self.GButton_893.place(x=530,y=560,width=100,height=35)
        self.GButton_893["command"] = self.GButton_893_command

    def GButton_129_command(self):
        try:
            path = filedialog.askopenfile(filetypes=(('.json', '*.json'),), initialdir="./")
            self.cities_names, self.cities_coords = fun.open_file_json(path.name)
            self.num_nodi = len(self.cities_names)
            self.GLabel_360.configure(text=str(self.num_nodi))
            self.GLabel_194.configure(text=" " + path.name)
            self.GButton_95["state"] = "normal"
            self.GLineEdit_296["state"] = "normal"
        except(AttributeError):
            pass
        except:
            self.GButton_95["state"] = "disable"
            self.GLineEdit_296["state"] = "disable"
            tkinter.messagebox.showerror("Errore on open file!", message="Json file must have next informations:\n"
                                                                              "city"": ""(str)CityName,\n"
                                                                              "lat"": ""(float)lat,\n"
                                                                              "lng"": ""(float)lng\n")

    def start_algorithm(self):
        self.GButton_129["state"] = "disable"
        self.GLineEdit_296["state"] = "disable"
        self.GButton_95["state"] = "disable"
        self.GButton_450["state"] = "disable"
        self.GButton_893["state"] = "disable"
        self.GButton_200["state"] = "normal"
        self.GListBox_26.delete(0, tk.END)
        self.GListBox_280.delete(0, tk.END)
        self.stop = False
        self.start_time = 0
        self.stop_time = 0
        self.inter_time = 0
        t = Thread(target=self.tb_heuristic)
        t.start()


    def tb_heuristic(self):

        self.GListBox_26.insert("end", "Start Algorithm at 0s")
        self.start_time = time.perf_counter()
        medians = random.sample(self.cities_names, self.p)
        z = fun.fun_obj(self.cities_names, self.distance_matrix, medians)

        self.inter_time = time.perf_counter()
        self.GListBox_26.insert("end",  "[" + str(round(self.inter_time - self.start_time,1)) + "s]: Start Solution")
        self.GListBox_26.insert("end", "Z => " + str(z))
        self.GListBox_26.insert("end", "P-Mediane => " + str(medians))
        self.Label_119["text"] = "0.0"
        bad_medians = []
        end_loop = False
        k = 1
        while end_loop == False and self.stop == False and k < 1000:
            savings = {}
            max_val = -1
            cont_negative = 0
            for j in self.cities_names:
                if not (j in medians) and not (j in bad_medians):
                    cont = 0
                    for i in medians:
                        tmp_median = medians.copy()
                        tmp_median[tmp_median.index(i)] = j
                        z_new = fun.fun_obj(self.cities_names, self.distance_matrix, tmp_median)
                        savings[(i, j)] = z - z_new
                        if savings[(i, j)] < 0:
                            cont_negative = cont_negative + 1
                            cont = cont + 1
                        else:
                            if savings[(i, j)] > max_val:
                                max_val = savings[(i, j)]
                                best_z = z_new
                                best_medians = tmp_median.copy()
                    if cont == self.p:
                        bad_medians.append(j)

            self.inter_time_1 = time.perf_counter()
            self.GListBox_26.insert("end", "|-------------------------------------|")
            if cont_negative != len(savings):
                medians = best_medians.copy()
                z = best_z
                self.GListBox_26.insert("end", "[" + str(round(self.inter_time_1 - self.start_time, 1)) + "s]: Solution " + str(k))
                self.GListBox_26.insert("end", "Z => " + str(z))
                self.GListBox_26.insert("end", "P-Medians => " + str(medians))
                self.GListBox_26.insert("end", "Savings calculated => " + str(len(savings)))
                self.GListBox_26.insert("end", "Nodes excluded =>" + str(len(bad_medians)))
                self.GListBox_26.yview_scroll(10000000, "units")
                self.GListBox_26.xview_scroll(-10000000, "units")
                k = k + 1
            else:
                self.GListBox_26.insert("end", "[" + str(round(self.inter_time_1 - self.start_time, 1)) + "s]: Best Solution ")
                self.GListBox_26.insert("end", "Z => " + str(z))
                self.GListBox_26.insert("end", "P-Medians => " + str(medians))
                self.GListBox_26.yview_scroll(10000000, "units")
                self.GListBox_26.xview_scroll(-10000000, "units")
                end_loop = True
                self.z = z
                self.Label_119.configure(text=str(round(self.z,2)))
                self.medians = medians

                cont_i = 1
                for i in self.medians:
                    self.GListBox_280.insert("end", str(cont_i) + ") " + i)
                    cont_i = cont_i + 1
        if self.stop == True:
            self.GListBox_26.insert("end", "Forced stop.")
            self.GButton_450["state"] = "disable"
            self.GButton_893["state"] = "disable"
        else:
            self.GButton_450["state"] = "normal"
            self.GButton_893["state"] = "normal"
        self.GLineEdit_296["state"] = "normal"
        self.GButton_95["state"] = "normal"
        self.GButton_129["state"] = "normal"
        self.GButton_200["state"] = "disable"

    def GButton_95_command(self):
        val = self.GLineEdit_296.get()
        error = 0
        if len(val) == 0:
            error = 1
        else:
            for i in val:
                if not(i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                    error = 1
        if error == 0:
            if int(val) <= 0 or int(val) > self.num_nodi:
                error = 1
        if error == 1:
            tkinter.messagebox.showerror("Error in P!", message="You must insert a number > 0!")
        else:
            self.GLineEdit_296["state"] = "disable"
            self.p = int(val)
            self.distance_matrix = fun.distance_matrix_generator(self.cities_names, self.cities_coords)
            self.z = 0.0
            self.medians = []
            self.start_algorithm()


    def GButton_200_command(self):
        self.stop = True
        self.GButton_450["state"] = "disable"
        self.GButton_893["state"] = "disable"
        self.GListBox_26.insert("end", "Force stopping...")



    def GButton_893_command(self):
        cluster_matrix = fun.assegnamento(self.distance_matrix, self.cities_names, self.medians)
        mappa = fun.map_generator(cluster_matrix, self.medians, self.cities_coords)
        mappa.save("./mappa.html")
        webbrowser.open("mappa.html")


    def GButton_450_command(self):
        content =  self.GListBox_26.get(0, tk.END)
        cont = 0

        try:
            f = filedialog.asksaveasfile(mode="w", defaultextension='.txt', filetypes=[(".txt", '*.txt')],initialdir="./",
                                         initialfile="log_heuristic.txt")
            for i in content:
                f.write(str(cont) + ". ")
                f.write(i)
                f.write("\n")
                cont = cont + 1
            f.close()
        except:
            pass


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
