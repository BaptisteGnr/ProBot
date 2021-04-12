from selenium import webdriver
import time
import webbrowser

Mdp = "BaptisteGarnier2005."

def Student_connection(username, password):
    _Username = username
    _Password = password

    time.sleep(1)

    #creer la variable qui gere le moteur de recherce
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.touraine-eschool.fr/portail/f/welcome/normal/render.uP")

    #Boutton d'identification de l'ent
    Identification_button = driver.find_element_by_id("portalCASLoginLink")
    Identification_button.click()

    #Bouton acces eleve/parent
    driver.find_element_by_class_name("parentEleveEN-IdP").click()

    #Remplissage du nom d'utilisateur
    input_username = driver.find_element_by_id("username")
    input_username.send_keys(_Username)

    #Remplissage du Mot de passe
    input_username = driver.find_element_by_id("password")
    input_username.send_keys(_Password)

    #Bouton Valider
    driver.find_element_by_id("bouton_valider").click()

    #Ouverture du menu de navigation (vissco)
    Navigation_button = driver.find_element_by_id("portlet_u19l1n81")
    Navigation_button.click()

    webbrowser.open_new_tab(driver.get("https://lycees.netocentre.fr/portail/api/ExternalURLStats?fname=VieScolaire&service=/esco-apps-redirector/index.php?appli=VIESCOLAIRE"))

def teacher_connection(username,password):
    _Username = username
    _Password = password

    time.sleep(1)

    #creer la variable qui gere le moteur de recherce
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.touraine-eschool.fr/portail/f/welcome/normal/render.uP")

    #Boutton d'identification de l'ent
    Identification_button = driver.find_element_by_id("portalCASLoginLink")
    Identification_button.click()

    #Bouton acces eleve/parent
    driver.find_element_by_class_name("catel-IdP").click()

    #Remplissage du nom d'utilisateur
    input_username = driver.find_element_by_id("user")
    input_username.send_keys(_Username)

    #Remplissage du Mot de passe
    input_username = driver.find_element_by_id("password")
    input_username.send_keys(_Password)

    #Bouton Valider
    driver.find_element_by_id("button").click()

    #Ouverture du menu de navigation (vissco)
    Navigation_button = driver.find_element_by_id("portlet_u19l1n81")
    Navigation_button.click()


def Student_College_connection(username, password):
    _Username = username
    _Password = password

    time.sleep(1)

    #creer la variable qui gere le moteur de recherce
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.touraine-eschool.fr/portail/f/welcome/normal/render.uP")

    #Boutton d'identification de l'ent
    Identification_button = driver.find_element_by_id("portalCASLoginLink")
    Identification_button.click()

    #Bouton acces eleve/parent
    driver.find_element_by_class_name("parentEleveEN-IdP").click()

    #Remplissage du nom d'utilisateur
    input_username = driver.find_element_by_id("username")
    input_username.send_keys(_Username)

    #Remplissage du Mot de passe
    input_username = driver.find_element_by_id("password")
    input_username.send_keys(_Password)

    #Bouton Valider
    driver.find_element_by_id("bouton_valider").click()

    #Ouverture du menu de navigation (vissco)
    Navigation_button = driver.find_element_by_id("portlet_u19l1n81")
    Navigation_button.click()

    webbrowser.open_new_tab(driver.get("https://www.touraine-eschool.fr/portail/api/ExternalURLStats?fname=VieScolaire&service=/esco-apps-redirector/index.php?appli=VIESCOLAIRE"))



