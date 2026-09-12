#!/usr/bin/env python3
"""
Launcher interactif pour Jarvis Discord Bot
Gère le démarrage, la configuration et la gestion du bot
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import Optional
import time


class JarvisLauncher:
    """Classe pour gérer le lancement du bot Jarvis"""
    
    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.venv_dir = self.root_dir / "venv"
        self.env_file = self.root_dir / ".env"
        self.requirements_file = self.root_dir / "requirements.txt"
        self.main_file = self.root_dir / "main.py"
        
    def clear_screen(self):
        """Efface l'écran du terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        """Affiche la bannière du launcher"""
        print("""
╔════════════════════════════════════════════════════════════╗
║                   🤖 JARVIS LAUNCHER 🤖                    ║
║            Discord Bot - Configuration & Lancement         ║
╚════════════════════════════════════════════════════════════╝
        """)
    
    def print_menu(self):
        """Affiche le menu principal"""
        print("\n📋 Menu Principal:")
        print("─" * 50)
        print("1️⃣  Démarrer le bot")
        print("2️⃣  Configuration rapide")
        print("3️⃣  Installer/Mettre à jour les dépendances")
        print("4️⃣  Créer un environnement virtuel")
        print("5️⃣  Vérifier l'installation")
        print("6️⃣  Ouvrir le fichier .env")
        print("7️⃣  Afficher les logs")
        print("0️⃣  Quitter")
        print("─" * 50)
    
    def check_python_version(self) -> bool:
        """Vérifie la version de Python"""
        version = sys.version_info
        if version.major >= 3 and version.minor >= 8:
            print(f"✅ Python {version.major}.{version.minor}.{version.micro} détecté")
            return True
        else:
            print(f"❌ Python 3.8+ requis (détecté: {version.major}.{version.minor})")
            return False
    
    def check_env_file(self) -> bool:
        """Vérifie la présence du fichier .env"""
        if self.env_file.exists():
            print("✅ Fichier .env trouvé")
            return True
        else:
            print("❌ Fichier .env non trouvé")
            return False
    
    def check_requirements(self) -> bool:
        """Vérifie la présence du fichier requirements.txt"""
        if self.requirements_file.exists():
            print("✅ Fichier requirements.txt trouvé")
            return True
        else:
            print("❌ Fichier requirements.txt non trouvé")
            return False
    
    def check_venv(self) -> bool:
        """Vérifie la présence de l'environnement virtuel"""
        if self.venv_dir.exists():
            print("✅ Environnement virtuel trouvé")
            return True
        else:
            print("❌ Environnement virtuel non trouvé")
            return False
    
    def verify_installation(self):
        """Vérifie l'installation complète"""
        print("\n🔍 Vérification de l'installation...")
        print("─" * 50)
        
        checks = [
            ("Python", self.check_python_version),
            ("Environnement virtuel", self.check_venv),
            ("requirements.txt", self.check_requirements),
            ("Fichier .env", self.check_env_file),
        ]
        
        results = []
        for name, check_func in checks:
            print(f"\n{name}:")
            results.append(check_func())
        
        print("\n" + "─" * 50)
        if all(results):
            print("✅ Tout est prêt! Vous pouvez démarrer le bot.")
        else:
            print("⚠️  Des éléments manquent. Veuillez les configurer.")
        
        input("\n[Appuyez sur Entrée pour continuer...]")
    
    def create_venv(self):
        """Crée un environnement virtuel"""
        print("\n🔧 Création de l'environnement virtuel...")
        print("─" * 50)
        
        try:
            subprocess.run([sys.executable, "-m", "venv", str(self.venv_dir)], 
                         check=True, cwd=str(self.root_dir))
            print("✅ Environnement virtuel créé avec succès!")
            
            print("\n📝 Prochaines étapes:")
            if os.name == 'nt':
                print(f"   1. Activez: .\\venv\\Scripts\\activate")
            else:
                print(f"   1. Activez: source venv/bin/activate")
            print(f"   2. Installez les dépendances: pip install -r requirements.txt")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur lors de la création du venv: {e}")
        
        input("\n[Appuyez sur Entrée pour continuer...]")
    
    def install_requirements(self):
        """Installe les dépendances"""
        print("\n📦 Installation des dépendances...")
        print("─" * 50)
        
        if not self.venv_dir.exists():
            print("❌ L'environnement virtuel n'existe pas!")
            response = input("Voulez-vous le créer maintenant? (y/n): ").lower()
            if response == 'y':
                self.create_venv()
            else:
                return
        
        pip_executable = self.venv_dir / ("Scripts\\pip" if os.name == 'nt' else "bin/pip")
        
        try:
            subprocess.run([str(pip_executable), "install", "-r", str(self.requirements_file)],
                         check=True, cwd=str(self.root_dir))
            print("\n✅ Dépendances installées avec succès!")
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Erreur lors de l'installation: {e}")
        
        input("\n[Appuyez sur Entrée pour continuer...]")
    
    def run_setup(self):
        """Lance le script de configuration"""
        print("\n⚙️  Lancement de la configuration...")
        print("─" * 50)
        
        setup_file = self.root_dir / "setup.py"
        
        if not setup_file.exists():
            print("❌ Le fichier setup.py n'existe pas!")
            input("\n[Appuyez sur Entrée pour continuer...]")
            return
        
        try:
            subprocess.run([sys.executable, str(setup_file)], 
                         check=True, cwd=str(self.root_dir))
        except subprocess.CalledProcessError as e:
            print(f"❌ Erreur: {e}")
        
        input("\n[Appuyez sur Entrée pour continuer...]")
    
    def start_bot(self):
        """Démarre le bot"""
        print("\n🚀 Démarrage du bot Jarvis...")
        print("─" * 50)
        
        # Vérifications préalables
        if not self.check_env_file():
            print("❌ Fichier .env manquant!")
            response = input("Voulez-vous configurer le bot maintenant? (y/n): ").lower()
            if response == 'y':
                self.run_setup()
            else:
                input("\n[Appuyez sur Entrée pour continuer...]")
                return
        
        if not self.main_file.exists():
            print("❌ Le fichier main.py n'existe pas!")
            input("\n[Appuyez sur Entrée pour continuer...]")
            return
        
        python_executable = self.venv_dir / ("Scripts\\python" if os.name == 'nt' else "bin/python")
        
        if not python_executable.exists():
            python_executable = sys.executable
        
        try:
            print("\n✅ Bot en cours de démarrage...")
            print("💡 Appuyez sur Ctrl+C pour arrêter le bot\n")
            time.sleep(1)
            
            subprocess.run([str(python_executable), str(self.main_file)], 
                         cwd=str(self.root_dir))
        except KeyboardInterrupt:
            print("\n\n⏹️  Bot arrêté par l'utilisateur")
        except Exception as e:
            print(f"❌ Erreur lors du démarrage: {e}")
        
        input("\n[Appuyez sur Entrée pour continuer...]")
    
    def open_env_file(self):
        """Ouvre le fichier .env avec l'éditeur par défaut"""
        print("\n📝 Ouverture du fichier .env...")
        print("─" * 50)
        
        if not self.env_file.exists():
            print("❌ Le fichier .env n'existe pas!")
            response = input("Voulez-vous le créer via la configuration? (y/n): ").lower()
            if response == 'y':
                self.run_setup()
            input("\n[Appuyez sur Entrée pour continuer...]")
            return
        
        try:
            if os.name == 'nt':  # Windows
                os.startfile(str(self.env_file))
            elif sys.platform == 'darwin':  # macOS
                subprocess.run(['open', str(self.env_file)])
            else:  # Linux
                subprocess.run(['xdg-open', str(self.env_file)])
            
            print("✅ Fichier .env ouvert!")
        except Exception as e:
            print(f"❌ Impossible d'ouvrir le fichier: {e}")
            print(f"   Chemin: {self.env_file}")
        
        input("\n[Appuyez sur Entrée pour continuer...]")
    
    def show_logs(self):
        """Affiche les logs du bot"""
        print("\n📋 Logs du bot:")
        print("─" * 50)
        
        logs_dir = self.root_dir / "logs"
        
        if not logs_dir.exists():
            print("❌ Aucun fichier de logs trouvé")
            input("\n[Appuyez sur Entrée pour continuer...]")
            return
        
        log_files = list(logs_dir.glob("*.log"))
        
        if not log_files:
            print("❌ Aucun fichier de logs trouvé")
            input("\n[Appuyez sur Entrée pour continuer...]")
            return
        
        # Affiche le dernier log
        latest_log = max(log_files, key=lambda p: p.stat().st_mtime)
        
        try:
            with open(latest_log, 'r', encoding='utf-8') as f:
                content = f.read()
                # Affiche les dernières 30 lignes
                lines = content.split('\n')
                print(f"\n📄 {latest_log.name}")
                print("─" * 50)
                print('\n'.join(lines[-30:]))
        except Exception as e:
            print(f"❌ Erreur lors de la lecture: {e}")
        
        input("\n[Appuyez sur Entrée pour continuer...]")
    
    def run(self):
        """Boucle principale du launcher"""
        while True:
            self.clear_screen()
            self.print_banner()
            self.print_menu()
            
            choice = input("Choisissez une option (0-7): ").strip()
            
            if choice == '1':
                self.start_bot()
            elif choice == '2':
                self.run_setup()
            elif choice == '3':
                self.install_requirements()
            elif choice == '4':
                self.create_venv()
            elif choice == '5':
                self.verify_installation()
            elif choice == '6':
                self.open_env_file()
            elif choice == '7':
                self.show_logs()
            elif choice == '0':
                print("\n👋 Au revoir!")
                sys.exit(0)
            else:
                print("❌ Option invalide!")
                input("[Appuyez sur Entrée pour continuer...]")


def main():
    """Point d'entrée du launcher"""
    try:
        launcher = JarvisLauncher()
        launcher.run()
    except KeyboardInterrupt:
        print("\n\n👋 Launcher fermé")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
