while True:
    a = print("""
      **   *******       **      ********
     /**  **/////**     ****    **////// 
     /** **     //**   **//**  /**       
     /**/**      /**  **  //** /*********
     /**/**      /** **********////////**
 **  /**//**     ** /**//////**       /**
//*****  //*******  /**     /** ******** 
 /////    ///////   //      // ////////  
    """)
    print("Bem vindo a Ferramenta de Facebook Stalking v2.0\n")
    print("Para o uso da ferramenta só coloque o numero de ID perfil\n")
    print("Exemplo: Facebook.com/numerodoperfil\n")
    print("OBS: O nome do perfil não é valido e sim os numéros, caso deseja saber o ID de alguém só acessar o site: https://findmyfbid.com/")
    print("\n1 - Tag\n2 - Comentários\n3 - Gostei\n4 - Locais\n5 - Social\n6 - Interesses")
    menu = input("Digite a opção desejada: ")
    if menu == "1":
        a = """ _________ __                       
 /   _____//  |_  ___________ ___.__.
 \_____  \\   __\/  _ \_  __ <   |  |
 /        \|  | (  <_> )  | \/\___  |
/_______  /|__|  \____/|__|   / ____|
        \/                    \/     """
        print(a)
        tag = input("Digite o número do perfil: ")
        print("Fotos: ")
        print(f"https://www.facebook.com/search/{tag}/photos-of/")
        print("Videos: ")
        print(f"https://www.facebook.com/search/{tag}/videos-of/")
        print("Postagens: ")
        print(f"https://www.facebook.com/search/{tag}/stories-tagged/")
    if menu == "2":
        b = """
_________                               __               .__              
\_   ___ \  ____   _____   ____   _____/  |______ _______|__| ____  ______
/    \  \/ /  _ \ /     \_/ __ \ /    \   __\__  \\_  __ \  |/  _ \/  ___/
\     \___(  <_> )  Y Y  \  ___/|   |  \  |  / __ \|  | \/  (  <_> )___ \ 
 \______  /\____/|__|_|  /\___  >___|  /__| (____  /__|  |__|\____/____  >
        \/             \/     \/     \/          \/                    \/  """
        print(b)
        comentario = input("Digite o número do perfil: ")
        print("Fotos: ")
        print(f"https://www.facebook.com/search/{comentario}/photos-commented/")
        print("Videos: ")
        print(f"https://www.facebook.com/search/{comentario}/videos-commented/")
        print("Postagens: ")
        print(f"https://www.facebook.com/search/{comentario}/stories-commented/")
    if menu == "3":
        c = """
  ________                __         
 /  _____/  ____  _______/  |_  ____ |__|
/   \  ___ /  _ \/  ___/\   __\/ __ \|  |
\    \_\  (  <_> )___ \  |  | \  ___/|  |
 \______  /\____/____  > |__|  \___  >__|
        \/           \/            \/     """
        print(c)
        gostei = input("Digite o número do perfil: ")
        print("Fotos: ")
        print(f"https://www.facebook.com/search/{gostei}/photos-liked/")
        print("Videos: ")
        print(f"https://www.facebook.com/search/{gostei}/videos-liked/")
        print("Postagens: ")
        print(f"https://www.facebook.com/search/{gostei}/stories-liked/")
    if menu == "4":
        d = """
.____                        .__        
|    |    ____   ____ _____  |__| ______
|    |   /  _ \_/ ___\__  \ |  |/  ___/
|    |__(  <_> )  \___ / __ \|  |\___ \ 
|_______ \____/ \___  >____  /__/____  >
        \/          \/     \/        \/ 
        """
        print(d)
        local = input("Digite o número do perfil: ")
        print("Locais: ")
        print(f"https://www.facebook.com/search/{local}/places-visited/")
    if menu == "5":
        e = """
_________             .__       .__   
 /   _____/ ____   ____ |__|____  |  |  
 \_____  \ /  _ \_/ ___\|  \__  \ |  |  
 /        (  <_> )  \___|  |/ __ \|  |__
/_______  /\____/ \___  >__(____  /____/
        \/            \/        \/      
        """
        print(e)
        social = input("Digite o número do perfil: ")
        print("Familia: ")
        print(f"https://www.facebook.com/search/{social}/relatives/intersect")
        print("Amigos: ")
        print(f"https://www.facebook.com/search/{social}/friends/intersect")
        print("Amigos de Amigos: ")
        print(f"https://www.facebook.com/search/{social}/friends/friends/intersect")
    if menu == "6":
        f = """
.___        __                                                    
|   | _____/  |_  ___________   ____   ______ ______ ____   ______
|   |/    \   __\/ __ \_  __ \_/ __ \ /  ___//  ___// __ \ /  ___/
|   |   |  \  | \  ___/|  | \/\  ___/ \___ \ \___ \\  ___/ \___ \ 
|___|___|  /__|  \___  >__|    \___  >____  >____  >\___  >____  >
         \/          \/            \/     \/     \/     \/     \/ 
        """
        print(f)
        interesses = input("Digite o número do perfil: ")
        print("Páginas de interesse: ")
        print(f"https://www.facebook.com/search/{interesses}/pages-liked/intersect")
        print("Locais de interesse: ")
        print(f"https://www.facebook.com/search/{interesses}/places-liked/intersect/")

