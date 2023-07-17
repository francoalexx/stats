import typing
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel ,QComboBox, QWidget, QPushButton, QScrollArea, QMenuBar, QStatusBar, QTextEdit, QCheckBox
from PyQt5 import uic
import sys
import pandas as pd
from PyQt5.QtCore import Qt

##########################################################

lebron_file = pd.read_csv("lestats.csv")
curry_file = pd.read_csv("curry_stats.csv")
shaq_file = pd.read_csv('shaq_stats.csv')
kobe_file = pd.read_csv('kobe_stats.csv')
bam_file = pd.read_csv('bam_stats.csv')


#################################

games_before_recent = 0
beginning_stats = 0
end_of_stats = 0

###################################
 








###########################################################

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi('statsmuse.ui', self)

        with open("style.qss", "r") as f:
            _style = f.read()
            app.setStyleSheet(_style)

        self.button.clicked.connect(self.getOptions)

        self.print_button.clicked.connect(self.print)

        self.file = None

        self.show()

    def getOptions(self):
        chosen_player = self.comboBox.currentText()

        if chosen_player == "Lebron James":
            self.file = lebron_file
        if chosen_player == "Stephen Curry":
            self.file = curry_file
        if chosen_player == "Shaquille O'Neal":
            self.file = shaq_file
        if chosen_player == 'Kobe Bryant':
            self.file = kobe_file
        if chosen_player == 'Bam Adebayo':
            self.file = bam_file

####################################################
 
###################################################

###############################################


    def print(self):

#####################################

        if self.file is None:
            print("No file selected.")
            return
        global organizer
        chosen_stat = self.comboBox_2.currentText()
        chosen_year = self.machine.toPlainText()
        chosen_team = self.oppBox.currentText()
    
################################################
        def search_opponent_only(): 
            organizer = self.file.loc[:,"Year"]
            dates = self.file.loc[:,"Playoffs"]
            points = self.file.loc[:,"PTS"]
            assist = self.file.loc[:,"AST"]
            o_rbs = self.file.loc[:,"ORB"]
            d_rbs = self.file.loc[:,"DRB"]
            rebounds = self.file.loc[:,"TRB"]
            steals = self.file.loc[:,"STL"]
            blocks = self.file.loc[:,"BLK"]
            turnovers = self.file.loc[:,"TOV"]
            fouls = self.file.loc[:,"PF"]
            minutes = self.file.loc[:,"MP"]
            fieldgoals = self.file.loc[:,"FG"]
            fg_attempts = self.file.loc[:,"FGA"]
            fgp = self.file.loc[:,"FG%"]
            three_made = self.file.loc[:,"3P"]
            three_att = self.file.loc[:,"3PA"]
            tpp = self.file.loc[:,"3P%"]
            free_throws = self.file.loc[:,"FT"]
            ft_attempts = self.file.loc[:,"FTA"]
            ft_percentage = self.file.loc[:,"FT%"]
            opponent = self.file.loc[:,"Opp"]
            def pts():
                stats = {k: (v, o) for k, v, o in zip(dates, points, opponent)}
                return stats
            def assists():
                stats = {k: (v, o) for k, v, o in zip(dates, assist, opponent)}
                return stats
            def o_rebounds():
                stats = {k: (v, o) for k, v, o in zip(dates, o_rbs, opponent)}
                return stats
            def d_rebounds():
                stats = {k: (v, o) for k, v, o in zip(dates, d_rbs, opponent)}
                return stats
            def rbs():
                stats = {k: (v, o) for k, v, o in zip(dates, rebounds, opponent)}
                return stats
            def stl():
                stats = {k: (v, o) for k, v, o in zip(dates, steals, opponent)}
                return stats
            def blk():
                stats = {k: (v, o) for k, v, o in zip(dates, blocks, opponent)}
                return stats
            def tov():
                stats = {k: (v, o) for k, v, o in zip(dates, turnovers, opponent)}
                return stats
            def fls():
                stats = {k: (v, o) for k, v, o in zip(dates, fouls, opponent)}
                return stats
            def min():
                stats = {k: (v, o) for k, v, o in zip(dates, minutes, opponent)}
                return stats
            def fg():
                stats = {k: (v, o) for k, v, o in zip(dates, fieldgoals, opponent)}
                return stats
            def fg_att():
                stats = {k: (v, o) for k, v, o in zip(dates, fg_attempts, opponent)}
                return stats
            def fg_percentage():
                stats = {k: (v, o) for k, v, o in zip(dates, fgp, opponent)}
                return stats
            def threep_made():
                stats = {k: (v, o) for k, v, o in zip(dates, three_made, opponent)}
                return stats
            def threep_att():
                stats = {k: (v, o) for k, v, o in zip(dates, three_att, opponent)}
                return stats
            def tpoint_percentage():
                stats = {k: (v, o) for k, v, o in zip(dates, tpp, opponent)}
                return stats
            def free_throw():
                stats = {k: (v, o) for k, v, o in zip(dates, free_throws, opponent)}
                return stats
            def free_throw_att():
                stats = {k: (v, o) for k, v, o in zip(dates, ft_attempts, opponent)}
                return stats
            def free_throw_perc():
                stats = {k: (v, o) for k, v, o in zip(dates, ft_percentage, opponent)}
                return stats
            
            if chosen_stat == "Points":
                stats = pts()
            if chosen_stat == "Assists":
                stats = assists()
            if chosen_stat == 'Rebounds':
                stats == rbs()
            if chosen_stat == "Steals":
                stats = stl()
            if chosen_stat == 'Blocks':
                stats = blk()
            if chosen_stat == 'Fouls':
                stats = fls()
            if chosen_stat == "Free Throws":
                stats = free_throw()
            if chosen_stat == 'Three Pointers':
                stats = threep_made()
            if chosen_stat == 'Field Goals':
                stats = fg()
            print(stats)
            if chosen_team == 'Choose':
                dict_str = "\n".join([f"{key}: {value}" for key, value in stats.items()])
                self.printArea.setPlainText(dict_str)
                return
            keys_remove = []
            for key, (value1, value2) in stats.items():
                if value2 != str(chosen_team):
                    keys_remove.append(key)
            for key in keys_remove:
                stats.pop(key)
            dict_str = "\n".join([f"{key}: {value}" for key, value in stats.items()])
            self.printArea.setPlainText(dict_str)




###############################################
        if chosen_year == '':
            search_opponent_only()
            return
        chosen_year = int(chosen_year)

        organizer = self.file.loc[:,"Year"]
        dates = self.file.loc[:,"Playoffs"]
        points = self.file.loc[:,"PTS"]
        assist = self.file.loc[:,"AST"]
        o_rbs = self.file.loc[:,"ORB"]
        d_rbs = self.file.loc[:,"DRB"]
        rebounds = self.file.loc[:,"TRB"]
        steals = self.file.loc[:,"STL"]
        blocks = self.file.loc[:,"BLK"]
        turnovers = self.file.loc[:,"TOV"]
        fouls = self.file.loc[:,"PF"]
        minutes = self.file.loc[:,"MP"]
        fieldgoals = self.file.loc[:,"FG"]
        fg_attempts = self.file.loc[:,"FGA"]
        fgp = self.file.loc[:,"FG%"]
        three_made = self.file.loc[:,"3P"]
        three_att = self.file.loc[:,"3PA"]
        tpp = self.file.loc[:,"3P%"]
        free_throws = self.file.loc[:,"FT"]
        ft_attempts = self.file.loc[:,"FTA"]
        ft_percentage = self.file.loc[:,"FT%"]
        opponent = self.file.loc[:,"Opp"]

#####################################

        if self.yesBox.isChecked():
            def pts():
                stats = {k: (v, o) for k, v, o in zip(dates, points, opponent)}
                return stats
            def assists():
                stats = {k: (v, o) for k, v, o in zip(dates, assist, opponent)}
                return stats
            def o_rebounds():
                stats = {k: (v, o) for k, v, o in zip(dates, o_rbs, opponent)}
                return stats
            def d_rebounds():
                stats = {k: (v, o) for k, v, o in zip(dates, d_rbs, opponent)}
                return stats
            def rbs():
                stats = {k: (v, o) for k, v, o in zip(dates, rebounds, opponent)}
                return stats
            def stl():
                stats = {k: (v, o) for k, v, o in zip(dates, steals, opponent)}
                return stats
            def blk():
                stats = {k: (v, o) for k, v, o in zip(dates, blocks, opponent)}
                return stats
            def tov():
                stats = {k: (v, o) for k, v, o in zip(dates, turnovers, opponent)}
                return stats
            def fls():
                stats = {k: (v, o) for k, v, o in zip(dates, fouls, opponent)}
                return stats
            def min():
                stats = {k: (v, o) for k, v, o in zip(dates, minutes, opponent)}
                return stats
            def fg():
                stats = {k: (v, o) for k, v, o in zip(dates, fieldgoals, opponent)}
                return stats
            def fg_att():
                stats = {k: (v, o) for k, v, o in zip(dates, fg_attempts, opponent)}
                return stats
            def fg_percentage():
                stats = {k: (v, o) for k, v, o in zip(dates, fgp, opponent)}
                return stats
            def threep_made():
                stats = {k: (v, o) for k, v, o in zip(dates, three_made, opponent)}
                return stats
            def threep_att():
                stats = {k: (v, o) for k, v, o in zip(dates, three_att, opponent)}
                return stats
            def tpoint_percentage():
                stats = {k: (v, o) for k, v, o in zip(dates, tpp, opponent)}
                return stats
            def free_throw():
                stats = {k: (v, o) for k, v, o in zip(dates, free_throws, opponent)}
                return stats
            def free_throw_att():
                stats = {k: (v, o) for k, v, o in zip(dates, ft_attempts, opponent)}
                return stats
            def free_throw_perc():
                stats = {k: (v, o) for k, v, o in zip(dates, ft_percentage, opponent)}
                return stats
        else:

            def assists():
                stats = {k: v for k, v in zip(dates, assist)}
                return stats
            def o_rebounds():
                stats = {k: v for k, v in zip(dates, o_rbs)}
                return stats
            def d_rebounds():
                stats = {k: v for k, v in zip(dates, d_rbs)}
                return stats
            def rbs():
                stats = {k: v for k, v in zip(dates, rebounds)}
                return stats
            def stl():
                stats = {k: v for k, v in zip(dates, steals)}
                return stats
            def blk():
                stats = {k: v for k, v in zip(dates, blocks)}
                return stats
            def tov():
                stats = {k: v for k, v in zip(dates, turnovers)}
                return stats
            def fls():
                stats = {k: v for k, v in zip(dates, fouls)}
                return stats
            def min():
                stats = {k: v for k, v in zip(dates, minutes)}
                return stats
            def fg():
                stats = {k: v for k, v in zip(dates, fieldgoals)}
                return stats
            def fg_att():
                stats = {k: v for k, v in zip(dates, fg_attempts)}
                return stats
            def fg_percentage():
                stats = {k: v for k, v in zip(dates, fgp)}
                return stats
            def threep_made():
                stats = {k: v for k, v in zip(dates, three_made)}
                return stats
            def threep_att():
                stats = {k: v for k, v in zip(dates, three_att)}
                return stats
            def tpoint_percentage():
                stats = {k: v for k, v in zip(dates, tpp)}
                return stats
            def free_throw():
                stats = {k: v for k, v in zip(dates, free_throws)}
                return stats
            def free_throw_att():
                stats = {k: v for k, v in zip(dates, ft_attempts)}
                return stats
            def free_throw_perc():
                stats = {k: v for k, v in zip(dates, ft_percentage)}
                return stats
########################

            def pts():
                stats = {k: v for k, v in zip(dates, points)}
                return stats

        if chosen_stat == "Points":
            stats = pts()
        if chosen_stat == "Assists":
            stats = assists()
        if chosen_stat == 'Rebounds':
            stats = rbs()
        if chosen_stat == "Steals":
            stats = stl()
        if chosen_stat == 'Blocks':
            stats = blk()
        if chosen_stat == 'Fouls':
            stats = fls()
        if chosen_stat == "Free Throws":
            stats = free_throw()
        if chosen_stat == 'Three Pointers':
            stats = threep_made()
        if chosen_stat == 'Field Goals':
            stats = fg()
    

        



        def recent_year(date):
            global games_before_recent
            length_stats = len(organizer)
            recent_year = organizer[length_stats - 1]
            if recent_year == date:
                for x in organizer:
                    if x == date:
                        break
                    else:
                        games_before_recent += 1
        
        def print_stats_recent(stats, games_before_recent):
            stats_list = list(stats.items())
            del stats_list[:games_before_recent]
            stats = dict(stats_list)
            return stats
        
        def first_part(date):
            global beginning_stats
            if int(date) < 0:
                print('Error')
                return
            if date != 2006:
                for x in organizer:
                    if x == date:
                        break
                    else:
                        beginning_stats += 1
            else:
                beginning_stats = 0

            return beginning_stats
    
        def second_part(date, beginning_stats):
            global end_of_stats
            target = int(date) + 1

            while True:
                found = False
                for x in organizer:
                    if x == target:
                        found = True
                        break

                if found:
                    break
                else:
                    target += 1

            for x in organizer:
                if x == target:
                    break
                else:
                    end_of_stats += 1

            end_of_stats = end_of_stats - beginning_stats
            return end_of_stats

        def print_stats(stats, end_of_stats, beginning_stats):
            stats_list = list(stats.items())
            if beginning_stats >= len(stats_list):
                return []
            else:
                del stats_list[:beginning_stats]

            adjusted_stats = stats_list[:end_of_stats]

            stats = dict(adjusted_stats)
            return stats


        recent_year(chosen_year)
        first_part(chosen_year)
        second_part(chosen_year, beginning_stats)
        result = print_stats(stats, end_of_stats, beginning_stats)


###########################################################

        def search_opponent_only():
            def pts():
                stats = {k: (v, o) for k, v, o in zip(dates, points, opponent)}
                return stats
            def assists():
                stats = {k: (v, o) for k, v, o in zip(dates, assist, opponent)}
                return stats
            def o_rebounds():
                stats = {k: (v, o) for k, v, o in zip(dates, o_rbs, opponent)}
                return stats
            def d_rebounds():
                stats = {k: (v, o) for k, v, o in zip(dates, d_rbs, opponent)}
                return stats
            def rbs():
                stats = {k: (v, o) for k, v, o in zip(dates, rebounds, opponent)}
                return stats
            def stl():
                stats = {k: (v, o) for k, v, o in zip(dates, steals, opponent)}
                return stats
            def blk():
                stats = {k: (v, o) for k, v, o in zip(dates, blocks, opponent)}
                return stats
            def tov():
                stats = {k: (v, o) for k, v, o in zip(dates, turnovers, opponent)}
                return stats
            def fls():
                stats = {k: (v, o) for k, v, o in zip(dates, fouls, opponent)}
                return stats
            def min():
                stats = {k: (v, o) for k, v, o in zip(dates, minutes, opponent)}
                return stats
            def fg():
                stats = {k: (v, o) for k, v, o in zip(dates, fieldgoals, opponent)}
                return stats
            def fg_att():
                stats = {k: (v, o) for k, v, o in zip(dates, fg_attempts, opponent)}
                return stats
            def fg_percentage():
                stats = {k: (v, o) for k, v, o in zip(dates, fgp, opponent)}
                return stats
            def threep_made():
                stats = {k: (v, o) for k, v, o in zip(dates, three_made, opponent)}
                return stats
            def threep_att():
                stats = {k: (v, o) for k, v, o in zip(dates, three_att, opponent)}
                return stats
            def tpoint_percentage():
                stats = {k: (v, o) for k, v, o in zip(dates, tpp, opponent)}
                return stats
            def free_throw():
                stats = {k: (v, o) for k, v, o in zip(dates, free_throws, opponent)}
                return stats
            def free_throw_att():
                stats = {k: (v, o) for k, v, o in zip(dates, ft_attempts, opponent)}
                return stats
            def free_throw_perc():
                stats = {k: (v, o) for k, v, o in zip(dates, ft_percentage, opponent)}
                return stats
            
            if chosen_stat == "Points":
                stats = pts()
            if chosen_stat == "Assists":
                stats = assists()
            if chosen_stat == 'Rebounds':
                stats == rbs()
            if chosen_stat == "Steals":
                stats = stl()
            if chosen_stat == 'Blocks':
                stats = blk()
            if chosen_stat == 'Fouls':
                stats = fls()
            if chosen_stat == "Free Throws":
                stats = free_throw()
            if chosen_stat == 'Three Pointers':
                stats = threep_made()
            if chosen_stat == 'Field Goals':
                stats = fg()
            if self.yesBox.isChecked():
                keys_remove = []
                for key, (value1, value2) in stats.items():
                    if value2 != str(chosen_team):
                        keys_remove.append(key)
                for key in keys_remove:
                    result.pop(key)
                dict_str = "\n".join([f"{key}: {value}" for key, value in stats.items()])
                self.printArea.setPlainText(dict_str)
            else:
                dict_str = "\n".join([f"{key}: {value}" for key, value in stats.items()])
                self.printArea.setPlainText(dict_str)
            








#######################################
        if self.yesBox.isChecked():
            keys_remove = []
            for key, (value1, value2) in result.items():
                if value2 != str(chosen_team):
                    keys_remove.append(key)
            for key in keys_remove:
                result.pop(key)
            dict_str = "\n".join([f"{key}: {value}" for key, value in result.items()])
            self.printArea.setPlainText(dict_str)
        else:
            dict_str = "\n".join([f"{key}: {value}" for key, value in result.items()])
            self.printArea.setPlainText(dict_str)

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()