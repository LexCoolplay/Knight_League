from data_downloader import data_downloader
from data_downloader_weapons import weapon_downloader
from char import Charapter
from Equipment import Equipment
from Quest_downloader import Quest_downloader
class Game:
    def __init__(self):
        self.dic={}
        self.Hero=0


    def load_data(self):
        data=data_downloader('data.txt')
        weapons=weapon_downloader('weapons.txt')
        quests=Quest_downloader('quests.txt')
        self.arr=weapons.load()
        self.dic=data.load()
        self.quests=quests.load()


    def save_data(self):
        data=data_downloader('data.txt')
        weapons=weapon_downloader('weapons.txt')
        weapons.save(self.arr)
        data.save(self.dic)


    def register(self,name):
        if(name in self.dic.keys()):
            print("This name is already exist!")
        else:
            self.dic[name]=Charapter(name)
            self.save_data()
            print("Success!")


    def fight(self,name1,name2):
        if(name1 in self.dic.keys() and name2 in self.dic.keys()):
            if(self.dic[name1].call_power()>self.dic[name2].call_power()):
                print(name1,'wins!')
            elif(self.dic[name2]>self.dic[name1]):
                print(name2,'wins!')
            else:
                print('Draw!');
        else:
            print("One of the warriors isn't exist!")


    def forge(self,name,type,level_bonus,level):
        weapon=Equipment(name,type,level_bonus,level)
        if(weapon not in self.arr):
            self.arr[weapon.name]=weapon
            self.save_data()
            print("Successfuly added to weapons!")
        return weapon


    def ask_trade(self,weapon):
        print("You find:"+' '+weapon.call_info()+'.')
        x=input('Do you want to pick it up and drop your current weapon? Y/N ')
        if(x[0]=='Y'):
            if(weapon.type=='Armor'):
                self.Hero.Armor=weapon
            elif(weapon.type=='Inhand'):
                x=input('Which hand? L/R')
                if(x[0]=='L'):
                    self.Hero.Weapon_1=weapon
                else:
                    self.Hero.Weapon_2=weapon
            elif(weapon.type=='Magic'):
                self.Hero.Magic=weapon
        else:
            pass


    def log_in(self,name):
        if(name in self.dic.keys()):
            self.Hero=self.dic[name]
            print("Logged in Succesfuly!")
            return True
        else:
            print("No such charapter!")
            return False


    def start_quest(self,name):
        Mission=self.quests[name]
        success=Mission. calculate_perfomance(self.Hero.level)
        if(success==False and self.Hero.level!=1):
            print("Defeat!")
            self.Hero.level-=1
        elif(success==True):
            self.Hero.level+=1
        else:
            print("Victory!")
            self.Hero.level+=1
            self.ask_trade(self.arr[success])
