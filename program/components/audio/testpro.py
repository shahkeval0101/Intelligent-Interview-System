import components.audio.audio_main as mysp
import pickle
import os

def speech_analysis(filename):
    #print("filename", filename)
    local_path = os.getcwd()
    parent_path = os.path.dirname(local_path)
    #print("local_path     ",local_path)
    #p = os.path.join( str(local_path) ,"audio_wav1")
    #p="Walkers" *Audio file name
    #c=r"C:\Users\.......YOUR_NAME........\Desktop\myprosody" *an example of path to directory "myprosody" 
    #c = os.path.join( str(local_path),"myprosody")
    #print(p)
    #print(c)
    
    #p : path to dataset folder
    #m : path to file
    #m, p
    c = os.path.join(str(parent_path), "program", "components", "audio", "myprosody")
    #print("c         ",c)
    #mysp.mysptotal(c, filename)
    Gend_value = mysp.myspgend(c,filename)
    print(Gend_value)
    #mysp.myspsyl(c,filename)
    #mysp.mysppaus(c,filename)
    #mysp.myspsr(c,filename)
    #mysp.myspatc(c,filename)
    #mysp.myspst(c,filename)
    #mysp.myspod(c,filename)
    bal_value = mysp.myspbala(c,filename)
    print("balance=", bal_value, "# ratio (speaking duration)/(original duration)")
    #mysp.myspf0mean(c,filename)
    #mysp.myspf0sd(c,filename)
    #mysp.myspf0med(c,filename)
    #mysp.myspf0min(c,filename)
    #mysp.myspf0max(c,filename)
    #mysp.myspf0q25(c,filename)
    #mysp.myspf0q75(c,filename)
    pronoun_value = mysp.mysppron(c,filename)
    print("Pronunciation_posteriori_probability_score_percentage= :%.2f" % (pronoun_value))
    #mysp.myprosody(c,filename)
    acc_value = mysp.mysplev(c,filename)
    print(acc_value, "% accuracy in voice")
    return Gend_value, bal_value, pronoun_value, acc_value
    
#filename = r"C:\Users\keval\OneDrive\Desktop\Intelligent interview System\interviewer-system\student_interview_data\kevalshah90909@gmail\audio_wav1.wav"
#speech_analysis(filename)
    
