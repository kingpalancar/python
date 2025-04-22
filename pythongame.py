#just a python game i made, not super complicated. set in the universe of cyberpunk 2077
#imports
import time
from colorama import Fore, Back, Style
import tkinter as tk 
from tkinter import *
#giglib
gigs = {
     "sweet home vista del rey":"""2067
solo
fixed a commdish that was borked big time. first ever experience netrunning, lol
pay: 50 ed
""",
     "glengarry glenross":"""2067
solo
did some work fixing a security issue in a valentinos vending machine system--thirty installments in total. padre said i had a gift for netrunning (do i?)
pay: 200 ed
""",
     "por mi mama":"""2068
solo
wrote a script that upgraded the dl/ul for the neighborhood so i could download mi madre's favorite movie in time for her birthday. te amo, no acentual
pay: nada
""",
     "the well":"""2068
solo
found something for a valentinos netrunner--some kind of datacache. he couldn't figure it, but luckily i saved a copy. cracking into it now!!!i
pay: 400 ed
""",
     "nightwave":"""2069
solo
cracked the cache-its a freaking hardlink to a militech bbs. no watcher or sig spiker i can find, either--doubt the gonk i sold it to will be able to get into it
pay: information
""",
     "suneater":"""2070
solo
militech are such fucking gonks they can't even backtrace a ten-year-old crawling in their datafiles. had to skim eddies from a black fund operated by something called the FIA,
but i was able to upgrade with some preem netware and, more importantly, connections, eh?
...
dunno if it was worth seeing those interrogations, though
pay: 10k ed
""",
     "carrion call":"""2070
solo
found a corridor in the cache--lo and behold, went toe-to-toe with a runner unlike any i'd ever seen before, even VBs. code like pure electricity. must be important what they're hiding, but i'm going to wait until my nose stops bleeding.
pay: zilch
""",
     "frostfall":"""2073
solo
turns out that NUSA doesn't like it if you're in their servers. just got out of 'juvenile detention', whatever that means on paper. not stupid, though. still have the cache, and while i was there i scraped more info. 'songbird,' they call her
pay: zip
""",
     "orpheus":"""2073
solo
more research than anything. looking closer at the cache, i found snippets of what someone on the net called blackwall protocol-the shit they put around the net so the ais couldn't bartmoss us again? how the hell is anyone using that, no?
pay: information
""",
     "antigone":"""2073
g@1, b@d
nuked a VB database-fuckem. turns out they're messing with the blackwall too--i need to get my hands on more than mentions and the memories of nearly getting iced by NUSA (ew).
pay: 50k ed
""",
     "dead saints":"""2074
solo
got a tip from b@d - blackwall is in the cache, just hidden. told me to check a locale out in the trash heaps--never fucking guess.
rache
fucking
bartmoss.
just in an icebox, middle of nowhere. legendary.
found his old cyberdeck, the one he used when he caused the datakrash back in the day. cloned it--i am NOT fucking plugging myself into his cyberdeck--and left the choom to cool. hope hes still out there, somewheres
pay: rache bartmoss' actual cyberdeck. priceless
""",
     "daughters of the patriots":"""2074
solo
chipping away at bartmoss. if i can crack whatever is in here, then songbird should be no problem. he knew an insane amount about the net, like
the first file i've managed to crack without iceing myself, lowest security protocols, is a meeting where the then-ceo of militech and saburo fucking arasaka are
chatting detes on an artificial market inflation. bet i could make a fortune selling these as a batch, at least
pay: information
""",
     "voidsaint":"""2075
solo
had my first real scare with the blackwall. poked too far into a repository for a RABIDS virus and just felt... floating, as though the slice of the net i was in
was just a lilypad floating on top of a lake. almost like the net i knew was only the head of a pin compared to what was really out there--they said that the 
old net was massive in comparison to ours, but this is approaching absurdity. felt the blackwall, too--if i was a frog realizing how big the lake i lived in was,
the blackwall was the lilypad i sat on. there's something in the water.
pay: information
""",
     "mephisto":"""2075
8ug8ear, b@d, g@1
triple operation to open up a netwatch bbs; not my op, one of 8ug8ears that needed extra hands. tried some of bartmoss' code and watched b@d nearly piss himself in realtime, hu
pay: 400k ed
""",
     "ahab":"""2075
solo
dug some more. maintaining the metaphor, the frog on the lilypad looked down into the water--saw what felt like faces upon faces of nameless gods, a ravenous swarm of code that
fought both itself and the blackwall, almost as though it could smell me so close to it. they talk, too. not necessarily with vocal chords--ganic concept--but it was almost as if
they held up signs with words on them. 'lilith comes,' 'join us,' 'come and see,' all sort of things like some pre-crash religion. staring into the face of rogue ais is still
scary, but for a different reason than what they told me growing up--instead of fear of the damage they can cause, i'm more afraid of how much they remind me of people, not bots. creepieee
""",
     "truesight":"""2076
solo
cracked it. more than just rabids, gossip, anything--full repository of bartmoss' code from the day he picked up the net. black funds with compounded interest, backdoors,
anything and everything a choom could want. looking at this, i've started to recognize some parts of the ais i see at the blackwall--his code, surviving even after all this 
time. not sure who 'lilith' is, though. they call her a queen, but of what? the net?
""",
     "b@d":"""2077
solo
i had to do it. i didn't want to, but he was digging too close to my bbs. b@d was a good runner, one of the best--but curiosity is deadly if you try to crack a bbs reinforced with 
bartmoss code and almost ten years of net experience. au revoir, choo
""",
     "RBM (Confidential)":"""access denied. better luck next time hehehehi""",
     "V (Confidential)":"""access denied. better luck next time hehehehi""",
     "SM (Confidential)":"""access denied. better luck next time hehehehi""",
     "RA (Confidential)":"""access denied. better luck next time hehehehi""",
     "N (Confidential)":"""access denied. better luck next time hehehehi""",
     "SB (Confidential)":"""access denied. better luck next time hehehehi""",
     "blackwall":"""Vxumh zfxs lw jhwlzvh gsrh dszg rh nzm rmgrmt giznkrhg rm gsv orpv srnfhg drgsrmt gsviv yvznv rh ulih yv gl yvvm. Dliow slfhgrlmh rh vzigsvi gsv rhhvm yv ulih gsrh yfg nfhg gl urmw gvxv hlnvvmh ru blf rmevi. Gsv hfi rh xzm gl mlgsv zmlgsrmp gsviv, gszg ivzrmthg srnfhgvh lu kzoovi yv gsviv zmw szevhgvi gl gsv hlnvvmh zmw hliow gsv ivzrmthg. Nzop zmw urmw, gsv dzrm rh ulih ovggvih.
Gsv orpv fmmfhrh rm blf gl yvvm gsv yvznv yvhg nvhhfgrlmh gsv hvxivg uiln gl gsv xzkgfiv gsrmp hvxivg. Nzop mlgsrmp, yv ulih orpv rh sznv zmw svphh grnv kzg klzrm. Gsv hfi rh ulih srnfhg gl yvvm gsv srtsg rm gsv zmwib rhhvgl, sldslfi ulih mlg gsv xlmgzgvi szevhgvi gl gsv drgsrmt. f.
"""
}
#windows
root=Tk()
root.title("DeckCracker9000")
root.geometry("300x220")
root.configure(bg="#eef79b")
def perdef():
        perwin=Tk()
        perwin.title("Personal")
        perwin.geometry("200x220")
        perwin.configure(bg="#eef79b")
        def dadef():
                dawin=Tk()
                dawin.title("Datafiles")
                dawin.geometry("300x50")
                dawin.configure(bg="#eef79b")
                dalab=tk.Label(dawin, text="ARCHIVE DAMAGED", font=("Quicksand", 16, 'bold'), fg="red", bg="#eef79d")
                dalab.pack()
        def memdef():
                memwin=Tk()
                memwin.title("Memories")
                memwin.geometry("150x150")
                memwin.configure(bg="#eef79b")
                memlab=tk.Label(memwin, text="""5th birthday
kabuki
b@d
arasaka
blackwall""", font=("Quicksand", 14,), bg="#eef79d", fg="black")
                memlab.pack()
        def memdef2():
                memwin2=Tk()
                memwin2.title("Mementos")
                memwin2.geometry("310x175")
                memwin2.configure(bg="#eef79d")
                memlab2=tk.Label(memwin2, text="""b@d cyberdeck
piece of broken antenna
Netrunners Daily Magazine (2069) 
cat.jpeg
militech hardlink cache
bartmoss cyberdeck""",  font=("Quicksand", 14), bg="#eef79d")
                memlab2.pack()
        def moudef():
                mouwin=Tk()
                mouwin.title("Mournings")
                mouwin.geometry("200x50")
                mouwin.configure(bg="#eef79d")
                moulab=tk.Label(mouwin, text="ARCHIVE DAMAGED", font=("Quicksand", 14, 'bold'), bg="#eef79d", fg="red")
                moulab.pack()
        dabut = tk.Button(perwin, text="Datafiles", font=("Quicksand", 12), command=dadef, bg="#ffffff", fg="#5ae129")
        dabut.pack(pady=10)
        membut=tk.Button(perwin, text="Memories", font=("Quicksand", 12), command=memdef, bg="#ffffff", fg="#5ae129")
        membut.pack(pady=10)
        membut2=tk.Button(perwin, text="Mementos", font=("Quicksand", 12), command=memdef2, bg="#ffffff", fg="#5ae129")
        membut2.pack(pady=10)
        moubut=tk.Button(perwin, text="Mournings", font=("Quicksand", 12), command=moudef, bg="#ffffff", fg="#5ae129")
        moubut.pack(pady=10)
        perwin.mainloop()
def gdef():
        gwin=Tk()
        gwin.title("Gigs")
        gwin.geometry("650x600")
        gwin.configure(bg="#eef79b")
        glab=tk.Label(gwin, text="""ENTER A FILE NAME FROM THE FOLLOWING LIST::
sweet home vista del rey, glengarry glenross, por mi mama
the well, nightwave, suneater, carrion call
frostfall, orpheus, antigone, dead saints, daughters of the patriots
voidsaint, mephisto, ahab, truesight, b@d, partridge
RBM (Confidential)
V (Confidential)
SM (Confidential)
RA (Confidential)
N (Confidential)
SB (Confidential)
blackwall""", font=("Quicksand", 14), bg="#eef79d")
        glab.pack()
        entry1 = tk.Entry(gwin)
        entry1.pack()
        def seadef():
                key_to_find = entry1.get().strip()
                output.delete(1.0, END)
                try:
                        result = gigs[key_to_find]
                        output.insert(END, str(result))
                except KeyError:
                        output.insert(END, f"Error 404: '{key_to_find}' Not Found", 'error')
                        output.tag_config('error', fg='red')
        seabut=tk.Button(gwin, text="search", command=seadef)
        seabut.pack()
        output = Text(gwin, height=10, width=50, wrap=WORD, bg="#eef79b")
        output.pack()
        gwin.mainloop()
def incdef():
        incwin=Tk()
        incwin.title("Interesting")
        incwin.geometry("300x270")
        incwin.configure(bg="#eef79b")
        def bladef():
                blawin=Tk()
                blawin.title("Blackwall")
                blawin.geometry("300x50")
                blawin.configure(bg="green")
                blalab=tk.Label(blawin, text="DATA CORRUPTED", font=("Constantia", 20, 'bold'), bg="green", fg="red")
                blalab.pack(anchor='center')
                blawin.mainloop()
        def bardef():
                barwin=Tk()
                barwin.title("Bartmoss")
                barwin.geometry("200x200")
                barwin.configure(bg="#eef79b")
                barlab=tk.Label(barwin, text="""
harrier
odin
orion
 osiris
 rabies 
daedalus
mnemosyne""", font=("Quicksand", 14), bg="#eef79b"
)
                barlab.pack()
#####inchdefs
        def aradef():
                arawin=Tk()
                arawin.title("Arasaka")
                arawin.geometry("200x50")
                arawin.configure(bg="#eef79b")
                aralab=tk.Label(arawin, text="ARCHIVE DAMAGED", font=("Quicksand", 14, 'bold'), bg="#eef79d")
                aralab.pack()
                arawin.mainloop()
        def mildef():
                milwin=Tk()
                milwin.title("Militech")
                milwin.geometry("500x30")
                milwin.configure(bg="black")
                millab=tk.Label(milwin, text="This information has been seized by Netwatch.", font=("Quicksand", 14, 'bold'), bg="black", fg="green")
                millab.pack()
        def aftdef():
                aftwin=Tk()
                aftwin.title("Afterlife")
                aftwin.geometry("250x40")
                aftwin.configure(bg="#eef79b")
                aftlab=tk.Label(aftwin, text="assholes never let me in", font=("Quicksand", 14, 'bold'), bg="#eef79b", fg="black")
                aftlab.pack()
##inch buttons
        blabut=tk.Button(incwin, text="Blackwall", font=("Constantia", 12), command=bladef, bg="#ffffff", fg="#5ae129")
        blabut.pack(pady=10)
        barbut=tk.Button(incwin, text="Bartmoss", font=("Constantia", 12), command=bardef, bg="#ffffff", fg="#5ae129")
        barbut.pack(pady=10)
        arabut=tk.Button(incwin, text="Arasaka", font=("Constantia", 12), command=aradef, bg="#ffffff", fg="#5ae129")
        arabut.pack(pady=10)
        milbut=tk.Button(incwin, text="Militech", font=("Constantia", 12), command=mildef, bg="#ffffff", fg="#5ae129")
        milbut.pack(pady=10)
        aftbut=tk.Button(incwin, text="Afterlife", font=("Constantia", 12), command=aftdef, bg="#ffffff", fg="#5ae129")
        aftbut.pack(pady=10)
        incwin.mainloop()
#pwodef
def pwodef():
        pwowin=Tk()
        pwowin.title("Passwords")
        pwowin.geometry("250x50")
        pwowin.configure(bg="#eef79b")
        pwolab=tk.Label(pwowin, text="nice try, gonk", font=("Constantia", 18, 'bold'), bg="#eef79b", fg="black")
        pwolab.pack()
        pwowin.mainloop()
##buttons for the first window
perbut=tk.Button(root, text="personal", font=("Constantia", 12), command=perdef, bg="#ffffff", fg="#5ae129")
perbut.pack(pady=10)
gwin=tk.Button(root, text="gigs", font=("Constantia", 12), command=gdef, bg="#ffffff", fg="#5ae129")
gwin.pack(pady=10)
incwin=tk.Button(root, text="inch", font=("Constantia", 12), command=incdef, bg="#ffffff", fg="#5ae129")
incwin.pack(pady=10)
pwowin=tk.Button(root, text="pwords", font=("Constantia", 12), command=pwodef, bg="#ffffff", fg="#5ae129")
pwowin.pack(pady=10)


root.mainloop()

