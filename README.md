# Sams_Strip_Plot

How to Use (for Gianluca):

Until I add a GUI, its important to understand how this program actually works, the terminology I use, and what the experiments can tell you. 

At the very top of the script, add your peaklist files ***Make sure the peaks picked are in the same plan. In other words, do not use center peak*** If you don't have a peaklist file, that's fine, just leave it blank. Files should be entered as strings (like mine are)

There are 4 parameters you can modify. CA, CB, CO, and nitrogen [***This is the i nitrogen value]***. The nitrogen value is what everything will be refrenced to. It might be better to use the nitrogen value in the HNCA (or NOESY), since those will never change (unless you center peak, and if all the peaks were picked at the same time), but if you may accidently move your peak in the NHSQC you might come across some issues with the NOE matches. 

For i-1 searches, self explanatory. The CA will be the i-1 CA, same with CB. The CO will be the value in the HNCO (the program will search your HNCACO)
For i+1 search, again same thing. The CA and CB will be the i CA and CB now. The CO will be the value in your HNCACO (the program will search your HNCO)

This explains the multiple flags. The i-1 flags are self explanatory. The CA and CB values search through your HNCA and HNCACB (optimized or not, it doesn't matter). The CO searches through your HNCACO. The order describes what is being searched. 

I.E. If do '''CA_CB_flag=True''' Then the program will first match your CAs by looking at a strip plot of your HNCA with the CA value you gave it. Then it will look through your HNCACB at a strip plot of the CB value you gave it. It will only show the nitrogen value of the strip plot that contains both the CA and CB value. 

If you do '''CA_CO_flag=True''' Then the program as before, will first look at the CA. Then it will look at the HNCACO using the CO value you gave it. And only display the nitrogen value of the strip plot that contained both. 

For i+1, the i_CA stands for the HNCOCA. In addition to searching the HCNA spectra, it will also search the HNCOCA using the same CA value (sometimes the i-1 peak will show up in the HNCOCA where it won't in the HNCA, so it might be useful to look at just the HNCOCA matches too). The for flag (e.g. for_CA_CO) is for cases where the HNCO will be searched, instead of the HNCACO. Since you're going forward, the CO value will now be from your HNCACO [your i] , and will match the HNCO value. 

I.E. 
'''CA_CB_CO_i_CA_flag=True''' Will match the CA value to the HNCA. Then the CB to the HNCACB. Followed by the CO to the HNCO. And finally the CA to the HNCOCA. Only strips that contain matches in all 4 spectra will be shown. 

Finally, the main usefulness of this program, the NOE portion. Self explanatory. NH_flag will match the amide NOEs (range 6-12ppm), HA_flag will match the HA NOEs (3.5-6ppm). Only one peak in the i needs to match the NOE of w.e. ur searching for a match to show up. ***NOE strips are searched with the previous 3D matches. I.E. If your CA strip plot only found 5 matches, then only those 5 matches are searched***

The previous flags are what is run. They have no relation to what is displayed. ***If you want to run something, you must check its flag***. The display flags are just what is printed out. Maybe you want to see the HNCA matches, and the NOE matches. So you can check them to true. Maybe you only want to see the NOE matches, so you check the display CA flag as False. Again, these just display the output of the run itself, nothing more. There is an option to also display nitrogen values that are in both the NH match, and HA match (I only recommend using this in conjunction with the NH and HA matches, not as a replacement for them). 



