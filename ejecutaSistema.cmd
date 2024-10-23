dlv  KB\basico1.dl KB\perfilAlum.dl KB\caractePr1.dl -filter=asigna_final -n=5 > Adial1.int
dlv  KB\basico11.dl -filter=asigna_final -n=5 > Adial11.int

python outDlvToAdial1.py
python outDlvToAdial11.py

python genActB1.py
python genActB11.py

python extraeRcorrectas1.py > RespExamenes\RC1.txt
python extraeRcorrectas11.py > RespExamenes\RC11.txt

python simulaAlumnoEx1.py > RespExamenes\Ra1.txt
python simulaAlumnoEx11.py > RespExamenes\Ra11.txt

python califica1.py > califsLast\calif1.txt
python califica11.py > califsLast\calif11.txt

copy his\history.txt + RespExamenes\EncRa1.txt + RespExamenes\Ra1.txt +  RespExamenes\EncRa11.txt + RespExamenes\Ra11.txt+ RespExamenes\EncCalif1.txt +  califsLast\calif1.txt + RespExamenes\EncCalif11.txt + califsLast\calif11.txt  his\history.txt
