#!/usr/bin/env python3
"""
Script de démarrage rapide pour Jarvis Discord Bot
Optimisé pour un lancement instantané
"""

import os
import sys
import subprocess
from pathlib import Path
import json


class ViteStarter:
    """Classe pour démarrage rapide optimisé du bot"""
    
    def __init__(self):
        self.root_dir = Path(__file__).parent
        self.venv_dir = self.root_dir / "venv"
        self.env_file = self.root_dir / ".env"
        self.cache_file = self.root_dir / ".vite_cache"
        self.main_file = self.root_dir / "main.py"
    
    def load_cache(self) -> dict:
        """Charge le cache de la configuration"""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_cache(self, data: dict):
        """Sauvegarde le cache de la configuration"""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(data, f)
        except:
            pass
    
    def get_python_executable(self) -> str:
        """Obtient l'exécutable Python à utiliser"""
        python_executable = self.venv_dir / ("Scripts\\python" if os.name == 'nt' else "bin/python")
        
        if python_executable.exists():
            return str(python_executable)
        return sys.executable
    
    def quick_check(self) -> bool:
        """Vérification rapide avant le lancement"""
        checks = [
            ("Fichier .env", self.env_file.exists()),
            ("main.py", self.main_file.exists()),
        ]
        
        all_ok = True
        for name, exists in checks:
            if not exists:
                print(f"❌ {name} manquant")
                all_ok = False
        
        return all_ok
    
    def show_spinner(self, duration=2):
        """Affiche un spinner de chargement"""
        spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        import time
        end_time = time.time() + duration
        i = 0
        while time.time() < end_time:
            print(f'\r  {spinner[i % len(spinner)]} Démarrage...', end='', flush=True)
            time.sleep(0.1)
            i += 1
        print('\r' + ' ' * 30 + '\r', end='', flush=True)
    
    def start_fast(self):
        """Démarre le bot en mode rapide"""
        print("""
╔════════════════════════════════════════════╗
║     🚀 JARVIS - Démarrage Rapide 🚀       ║
╚════════════════════════════════════════════╝
        """)
        
        print("⚡ Vérification rapide...")
        
        if not self.quick_check():
            print("\n❌ Erreur: Configuration incomplète!")
            print("💡 Lancez d'abord: python launcher.py")
            return False
        
        print("✅ Configuration OK")
        
        self.show_spinner(1)
        
        python_exec = self.get_python_executable()
        
        print("\n🤖 Bot Jarvis en cours de démarrage...")
        print("💡 Appuyez sur Ctrl+C pour arrêter\n")
        
        try:
            subprocess.run([python_exec, str(self.main_file)], 
                         cwd=str(self.root_dir))
        except KeyboardInterrupt:
            print("\n\n⏹️  Bot arrêté")
        
        return True
    
    def start_with_args(self, args):
        """Démarre le bot avec des arguments personnalisés"""
        python_exec = self.get_python_executable()
        
        try:
            subprocess.run([python_exec, str(self.main_file)] + args, 
                         cwd=str(self.root_dir))
        except KeyboardInterrupt:
            print("\n\n⏹️  Bot arrêté")


def main():
    """Point d'entrée du script vite"""
    try:
        starter = ViteStarter()
        
        if len(sys.argv) > 1:
            # Si des arguments sont passés, les transmettre au bot
            starter.start_with_args(sys.argv[1:])
        else:
            # Sinon, démarrage rapide
            starter.start_fast()
    
    except KeyboardInterrupt:
        print("\n\n👋 Arrêt")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Erreur: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
