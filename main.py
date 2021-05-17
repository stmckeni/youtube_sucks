from __future__ import unicode_literals
import youtube_dl
import subprocess
import sys


from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import time
import traceback, sys
#global data storage
_001_ydl_status_data_deez_nutz = dict()
_974_goo_text = "flaggr"
# download video logger
class _download_video_logger(object):
    

    def debug(self, msg):
        
        print("fuckin debug")
        print(msg)
        print("debug is done")
        
        pass

    def warning(self,msg):
        
        print("this is a warning punk!!!")
        print(msg)
        pass
    
    def error(self,msg):
        
        print("Something broke so there's a fucking error, bitch")
        print(msg)
        print("can't even do this shit right")
        pass


def _msg_now_converting(d):
    if d['status'] == 'finished':
        print("shit is done so now we convert...")





#worker objects
class _worker_engine(QObject):
    
        
        finished = pyqtSignal()
        error = pyqtSignal(tuple)
        logger_signal = pyqtSignal(object)
        result = pyqtSignal(object)
        progress = pyqtSignal(int)
        directory = pyqtSignal(str)
        video_url = pyqtSignal(str)
        ydl_capture_signal = pyqtSignal()
        extension_connection = pyqtSignal(str)
        _download_mode = pyqtSignal(str)


#worker thread
class _download_worker(QRunnable):
    def __init__(self):
        super(_download_worker,self).__init__()
        self.signals = _worker_engine()
        self.ext = "mp3"
        self.ydl_opts = dict()
        self.ydl = 0
        self.logger_object = _download_video_logger()
        self._da_progress_number = 0
        self._da_status_text = "fag"
        self.youtube_or_video_url = "https://www.youtube.com/watch?v=3v7dmok7bI4"
        self._global_ydl_data = dict()
        global _001_ydl_status_data_deez_nutz
        global _974_goo_text 
        pass

    #set text object for the logger object
    def _set_logger_text_output_buffer(self,object):
        print(object)

    



    #progress data
    def _set_da_progress_data(self,inte):
        #self._da_progress_number = str(inte)
        if self._da_status_text == "fag":
            print("gay ass savages!!!!")
        

        _temp = int(self._da_progress_number)
        
        print("da progress is at")
        print(_temp)

    #set data extension
    def _set_da_mp3_or_mp4_extension(self,str):
        self.ext = str
        print("set da mp3 or mp4 extension connections called")
        print("ext data is (default setting is mp3):")
        print(self.ext)


    def _progress_bar_syncronizer(self,d):
        
        print("progress sync data")
        print(d)
        if d:
            _001_ydl_status_data_deez_nutz = d
            print("deez nuts?")
            print(_001_ydl_status_data_deez_nutz)
            self._global_ydl_data = _001_ydl_status_data_deez_nutz
            self._global_ydl_data = d
        if d['status'] == 'downloading':
            self._global_ydl_data = d
            print(d['downloaded_bytes'])
            print("faggot accident")
            print(self._global_ydl_data['_percent_str'])
            self._da_status_text = d['_percent_str'] 
            _974_goo_text = str(d['_percent_str'])
            self._da_progress_number = int(float(d['_percent_str'].replace("%","")))
            if _974_goo_text == self._da_status_text:
                print("links collide")
                print(_974_goo_text)
            print("now foe da percentage")
            print(d['_percent_str'])
        if d['status'] == 'finished':
            print("video downloaded")
         
    #download video or convert to audio
    def _set_download_mode(self,str):
        if str =="mp3":
            self.ydl_opts = {
            "format" : "bestaudio/best",
            "postprocessors" : [{
                "key":"FFmpegExtractAudio",
                "preferredcodec":self.ext,
                "preferredquality":"192",
            }],
            "logger":self.logger_object,
            "progress_hooks":[_msg_now_converting,self._progress_bar_syncronizer],

        }
        else:
            self.ydl_opts = {
            "format" : "bestvideo/best",
            "write_all_thumbnail":True,
            "include_ads":True,
            
            "logger":self.logger_object,
            "progress_hooks":[self._progress_bar_syncronizer],

        }

    #@pyqtSlot()
    def _set_video_url(self,str):
        self.youtube_or_video_url = str
        print("set video connect url shit")
        print(self.youtube_or_video_url +" test slot url for function")
        
    def _init_capture_of_download_unit(self):
        global _001_ydl_status_data_deez_nutz
        
        self.signals.extension_connection.connect(self._set_da_mp3_or_mp4_extension)

        self.signals._download_mode.connect(self._set_download_mode)
        self.signals.extension_connection.emit(self.ext)
        self._global_ydl_data = _001_ydl_status_data_deez_nutz
        if self.ext:
            self.signals._download_mode.emit(self.ext)

        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            

            
            
            self.ydl = ydl
            print("self ydl is")
            print(self.ydl)
            self._global_ydl_data = _001_ydl_status_data_deez_nutz

    
    def _download_protocol_001(self,object):
        print(object)
        self.signals.video_url.connect(self._set_video_url)
        self.signals.video_url.emit(self.youtube_or_video_url)
        self.signals.progress.emit(self._da_progress_number)
        self._global_ydl_data = _001_ydl_status_data_deez_nutz
        # with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
        #     print("this is what ydl is")
        #     print(ydl)
        self.ydl.download([self.youtube_or_video_url])
        self._global_ydl_data = _001_ydl_status_data_deez_nutz
        
        

            


    @pyqtSlot()
    def run(self):
        try:
            print("tried and true....")
            self._global_ydl_data = _001_ydl_status_data_deez_nutz
            self.signals.progress.connect(self._set_da_progress_data)
            self.signals.ydl_capture_signal.connect(self._init_capture_of_download_unit)
            self.signals.result.connect(self._download_protocol_001)
            self.signals.logger_signal.connect(self._set_logger_text_output_buffer)

        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            
            self.signals.error.emit((exctype,value,traceback.format_exc()))
        
        else:
            print("else hit after try...")
            self.signals.ydl_capture_signal.emit()
            
                    
            self.signals.result.emit("result flair")
            

        finally:     
               
            self.signals.finished.emit()





#download widget window
class _download_window_widget(QMainWindow):
    def __init__(self):
        super(_download_window_widget,self).__init__()
        self.setGeometry(400,100,500,500)

        self.file_name = "test_filename.mp(doesnotexist)"
        self.file_directory = "A://lisp"
        self._selected_extension = "mp4"
        self._progress_number = 0
        self._download_status_text = "download status"
        self.logger = _download_video_logger()
        self.generate_ui()
        self._generate_functions()

    def generate_ui(self):
        self._001_main_download_widget = QWidget()
        _9576_main_tmp_widget = self._001_main_download_widget
        _9576_main_tmp_widget.setWindowTitle("Downloading file..."+str(self.file_name))
        _9576_main_tmp_widget.setWindowIconText("Download da file")

        self._975_da_vbox = QVBoxLayout()
        _975_da_vbox = self._975_da_vbox
        self._09085_file_name_label = QLabel("Downloading dis file")
        _09085_file_name_label = self._09085_file_name_label
        _09085_file_name_label.setAlignment(Qt.AlignCenter)

        _975_da_vbox.addWidget(_09085_file_name_label)

        self._09085_file_download_status = QTextEdit("Loading status")

        
        self._09085_file_download_status.setText(self._download_status_text)
        self._09085_file_download_status.setAlignment(Qt.AlignCenter)
        _975_da_vbox.addWidget(self._09085_file_download_status)

        self._8hnt8bg_progress_bar = QProgressBar()
        self._8hnt8bg_progress_bar.setValue(self._progress_number)

        _975_da_vbox.addWidget(self._8hnt8bg_progress_bar)

        



        _9576_main_tmp_widget.setLayout(_975_da_vbox)

        self.setCentralWidget(self._001_main_download_widget)






    #make the thread functions work
    def _generate_functions(self):
        self.threadpool = QThreadPool()
           







_timer_tick = 0

class _001_da_splash_screen(QMainWindow):
    def __init__(self):
        super(_001_da_splash_screen,self).__init__()
        #set timer object 
        self._timer = QTimer(self)
        #set window properties
        self.setWindowFlags(Qt.Window | Qt.SplashScreen |Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        #progress bar
        self.progress_bar = QProgressBar(self)
        #Title
        self._001_title = QLabel("<strong>Youtube sucks</strong> <br/> Professional Offender <strong>&#174;</strong>")

        #self.setStyleSheet(_styx001F)

        self.initUI()

    def initUI(self):
        self.setGeometry(410,140,640,480)
        
        




      


        aImage = QImage("effyoutube.jpg")
        sImage = aImage.scaled(QSize(680,500))
        pallet = QPalette()
        pallet.setBrush(10,QtGui.QBrush(sImage))
        self.setPalette(pallet)

        
        

        
        self._001_title.setAlignment(Qt.AlignCenter)

        
        
        self._001_title.setStyleSheet("font-size:54px;background-color:blue;color:#ffff22;")
        
       
        
        
        #vbox
        _001_vbox = QVBoxLayout()
        #frame
        _001_frame = QFrame()
        #dynamic loading taskbar info
        self.setWindowTitle("Loading TurkeyBooks Pro...")

        #ver
        _001_verno = QLabel("<strong>Ver. 0.0.01</strong>")
        _001_verno.setAlignment(Qt.AlignCenter)
        
        _001_verno.setStyleSheet("color:#fefefe;font-size:37px;background-color:red;")
        
        
        
        #sub label
        self._001_stitle = QLabel("<strong>Loading...</strong> All Assets")
        self._001_stitle.setAlignment(Qt.AlignCenter)
        self._001_stitle.setStyleSheet("font-size:18px;color:limegreen;")



       
        #add frames and actions
       
        _001_vbox.addWidget(self._001_title)
        _001_vbox.addWidget(_001_verno)
        
      
        _001_vbox.addWidget(self._001_stitle)
        _001_vbox.addWidget(self.progress_bar)
        _001qwidget = QWidget()
        _001qwidget.setLayout(_001_vbox)
        
        self.setCentralWidget(_001qwidget)


        


        
        #display the stuff
        self.show()  


        #set loading splashscreen counter function
        self._timer.timeout.connect(self.opin_lid) 
        #start the timer 
        self._timer.start(35)

    #load information
    def opin_lid(self):
        #capture the global timer tick
        global _timer_tick

        if _timer_tick <= 101:
            #set progress bar
            self.progress_bar.setValue(_timer_tick)
            _timer_tick += 0.37449562384635648
            self._001_stitle.setText("<strong>Loading..</strong> "+str(_timer_tick)+"%")
            #loader tester
            # if _timer_tick >= 88.234:
            #     _timer_tick = 2.41
            

        else:    
            #dynamic loading taskbar info
            self.setWindowTitle("Software loaded...")
            self.main = _da_window()
            self.main.show()
            self._timer.stop()
            _timer_tick = 0
            self.close()



class _da_window(QMainWindow):
    def __init__(self):
        super(_da_window,self).__init__()
        self.setWindowTitle("Eff Youtube")

        self.setGeometry(400,100,500,500)


        self.setStyleSheet("background-color:aquablue;")

        #downloads object generator
        self._ooba = list()

        #conversion trigger
        self._03_output_ext = "mp3"
        #where to download the file to
        self._38hj58jg90_download_file_location = ""

        self.generate_UI()


    def generate_UI(self):
        _teity_vbox_layout = QVBoxLayout()

        _35_main_red_blit_widget = QWidget(self)
        _35_main_red_blit_widget.setStyleSheet("background-color:#ebebeb;")
       
        _4598_header = QLabel("YOUTUBE SUCKS SO HERE YOU GO")
        _4598_header.setAlignment(Qt.AlignCenter)

        _teity_vbox_layout.addWidget(_4598_header)


        self._0934j_url_video_box = QLineEdit()
        _0934j_url_video_box = self._0934j_url_video_box
        _0934j_url_video_box.setPlaceholderText("Youtube or video url here ex. http://url.com/")

        _0934j_url_video_box.setText("https://www.youtube.com/watch?v=qDEXfN2ifXY")



        _0934j_url_video_box.setAlignment(Qt.AlignCenter)


        _teity_vbox_layout.addWidget(_0934j_url_video_box)

        _934_groupBox_layout = QGroupBox("download video or music?")

        _934_group_hbox_layout = QHBoxLayout()
        #output conversion
        def _9357_convert_output(selected,s,a):
            
            if(selected and a.output_type=="music"):
                s._03_output_ext = "mp3"
                print(s._03_output_ext)
            else:
                s._03_output_ext = "mp4"
                print(s._03_output_ext)    

        _28474_q_radio_var = QRadioButton("video")

        _28474_q_radio_var.output_type = "video"

        _28474_q_radio_var.toggled.connect(lambda a:_9357_convert_output(a,self,_28474_q_radio_var))

        _934_group_hbox_layout.addWidget(_28474_q_radio_var)

        _28474_q_radio_audiovar = QRadioButton("music")

        _28474_q_radio_audiovar.output_type = "music"

        _28474_q_radio_audiovar.toggled.connect(lambda a:_9357_convert_output(a,self,_28474_q_radio_audiovar))

        _934_group_hbox_layout.addWidget(_28474_q_radio_audiovar)



        _934_groupBox_layout.setLayout(_934_group_hbox_layout)



        _teity_vbox_layout.addWidget(_934_groupBox_layout)

        def _30948_handle_file_location(a,s):
            if not a:
                _7456 = s.getExistingDirectory(None)
                
                self._38hj58jg90_download_file_location = _7456

                
        _934_file_location_dialog = QFileDialog(self,"save "+str(self._03_output_ext)+" file directory")

        
             

        

        _934_file_location_button = QPushButton("Save output location")

        _934_file_location_button.clicked.connect(lambda a:_30948_handle_file_location(a,_934_file_location_dialog))

        _teity_vbox_layout.addWidget( _934_file_location_button )

        

        _347_staart_download_button = QPushButton("Start Download")
        
        _347_staart_download_button.clicked.connect(lambda :self._standt_download())

        
        _teity_vbox_layout.addWidget(_347_staart_download_button)

        _35_main_red_blit_widget.setLayout(_teity_vbox_layout)
        self.setCentralWidget(_35_main_red_blit_widget)


    def _standt_download(self): 
        global _001_ydl_status_data_deez_nutz
        global _974_goo_text
        _ooba = self._ooba
        _ooba.append(_download_window_widget())
        _nbo_thread = _download_worker()
        #_download_window_widget()._8hnt8bg_progress_bar
        #_download_window_widget()._09085_file_download_status.append(str)
        print("deez fuckin nuts")
        print(_974_goo_text)
        print(_001_ydl_status_data_deez_nutz)
        
        self.timer = QTimer(self)
        self.timer.setInterval(3000)

        def _39048referesher(s,t):
           _zem_imemba = 0 
           if t._da_status_text == "fag":
               t._da_status_text = "0" 
               
           s._09085_file_download_status.setText(str(t._da_status_text))
           if type(t._da_status_text) == str:
            if t._da_status_text.find("%"):
                t._da_status_text.split("%")
                t._da_status_text.replace("%","")
                print("found to type of dat int")
                try:
                    _zem_imemba = int(t._da_status_text)
                except:
                    print("faild to convert string to text")
                    if type(_zem_imemba) == str:
                        _zem_imemba.replace("%","")
                        _zem_imemba = int(_zem_imemba)
                    print(t._da_status_text )
                    print(_zem_imemba)
           if type(t._da_progress_number) == str:
               if type(_zem_imemba) == str:
                   t._da_progress_number = int(_zem_imemba.replace("%",""))
                   s._8hnt8bg_progress_bar.setValue(t._da_progress_number)
           else:

               s._8hnt8bg_progress_bar.setValue(t._da_progress_number)    
           s._8hnt8bg_progress_bar.setValue(t._da_progress_number)

        
        

        
        for i in range(0,len(_ooba)):
            self.timer.timeout.connect(lambda : _39048referesher(_ooba[i],_nbo_thread))
            self.timer.start()
            _nbo_thread.signals.logger_signal.emit(_ooba[i]._09085_file_download_status)
            _ooba[i]._09085_file_download_status.append(_974_goo_text)
            #_ooba[i]._8hnt8bg_progress_bar.setValue(int(_001_ydl_status_data_deez_nutz['_percent_str']))
            
            _nbo_thread.ext = self._03_output_ext
            
            
            _nbo_thread.youtube_or_video_url = self._0934j_url_video_box.text()


            
            
            _ooba[i].show()
            _ooba[i].threadpool.start(_nbo_thread)

            
            
        #self.timer.stop()

























if __name__ == '__main__':
    #start the app sequence
    app = QApplication(sys.argv)
    #app.setStyleSheet(_styx001F)
    #init spashscreen
   # _st_001pimn = _001_da_splash_screen()
    _neep_dooka = _da_window()
    _neep_dooka.show()
   
    #win= _da_window()
    #exit software destroying resources and services in the process
    sys.exit(app.exec_())   


