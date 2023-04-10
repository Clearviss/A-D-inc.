import pyinputplus as po


while True:
    inp = po.inputYesNo('Chcesz sie dowiedziec jak zajac kogos godzinami?: ', yesVal='tak', noVal='nie')
    if inp == 'nie': 
        break
print('dziekuje, dowidzenia')
