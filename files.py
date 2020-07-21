# Creating files, check python file in finder and you will find the new file

#file = open("fun.text", "w") # w needs to create a file, r to read

#file.write("Hello my name is Nick\nThis is a new file")

print("\n")

# Reading files, when you open the file, you can write something and save it, and it will then appear here in python

#file2 = open("funread.text", "r") # r needs to read a file

#print(file2.read())
print("\n")

'''file = open("Coronavirus.text", "w") # Reading and Writing
file.write("""Non è la prima volta che il nostro paese si trova ad affrotnare emergenze nazionali. Stiamo affrontando la sfida del Coronavirus che non ha colore politico. Va vinta con l'impegno di tutti. L'Italia, tutta, è chiamata a fare la propria parte. Da gennaio, quando avevamo due casi, abbiamo messo in atto misure che sembravano drastiche ma che in realtà erano proporzionate a tutelare la diffusione del contagio e la salute dei cittadini. Abbiamo agito secondo la linea del comitato scientifico e la verità, la trasparenza, sono il primo vaccino di cui dotarci. Ho ritenuto doveroso spiegare a tutti i cittadini cosa stava accadendo. Siamo sulla stessa barca, chi ha il timone ha il dovere di indicare la rotta. Sono in arrivo nuove misure, serve uno sforzo in più, insieme. Il dato positivo è che in Italia la grandissima parte delle persone contagiate guariscono senza conseguenze. Una certa percentuale di persone necessita di un'assistenza continuata in terapia intensiva. In caso di crescita esponenziale di contagiati, nessun paese al mondo potrebbe affrontare una simile situazione di emergenza in termini di strutture, posti letto e risorse umane richieste. Per questa ragione il Ministro della Salute Speranza ha dato mandato nei giorni scorsi di aumentare del 50 per cento le unità di terapia intensiva e del 100 per cento le unità di terapia subintensiva. Non sarà possibile potenziarle in breve tempo, il primo obiettivo deve essere il contenimento del contagio. Non dobbiamo stravolgere le nostre abitudini ma dobbiamo assumere un comportamento responsabile. Evitiamo luoghi affollati. Da domani al 15 marzo saranno chiuse scuole ed atenei. Non si svolgeranno manifestazioni sportive con presenza del pubblico in modo da prevenire ulteriori occasioni di contagio. Già prima dell'emergenza Coronavirus avevo detto che l'economia italiana aveva bisogno di una terapia d'urto. Chiederemo all'Unione Europea tutta la flessibilità di bilancio di cui ci sarà bisogno per sostenere famiglie e imprese. Appronteremo un piano straordinario di opere pubbliche, serve mettere nuova finanza nell'economia e per alcuni investimenti valuteremo il modello Ponte Morandi. Sappiamo rialzarci, facendo squadra. Applicheremo il Modello Genova, sarà il Modello Italia. Sapremo superare questa difficoltà riaffermandoci nel nostro valore\n""")
'''
from os.path import join as pjoin
filename = "myfile.text"
path_to_file = pjoin("/Users/martina/PycharmProjects/pythonforprogrammers", filename)
FILE = open(path_to_file, "w")
Text = input("Write your story here: ")
FILE.write(Text)


