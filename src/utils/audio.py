import pygame
from pathlib import Path


class AudioManager:
    """Singleton class for managing sound playback."""
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        if not AudioManager._initialized:
            pygame.mixer.init()
            self.sounds = {}
            self.volume = 1.0
            
            # Load default sounds
            self.load_sound('hit_rock', 'assets/sounds/hit_rock.wav')
            
            AudioManager._initialized = True


    @staticmethod
    def get_instance():
        """Get the singleton instance."""
        if AudioManager._instance is None:
            AudioManager()
        return AudioManager._instance


    def load_sound(self, name: str, file_path: str) -> pygame.mixer.Sound:
        """Load a sound from file and cache it."""
        if name not in self.sounds:
            path = Path(file_path)
            if path.exists():
                self.sounds[name] = pygame.mixer.Sound(file_path)
                self.sounds[name].set_volume(self.volume)
            else:
                print(f"Warning: Sound file not found: {file_path}")
                return None
        return self.sounds.get(name)


    def play(self, name: str, loops: int = 0, maxtime: int = 0, fade_ms: int = 0):
        """Play a loaded sound."""
        if name not in self.sounds:
            print(f"Warning: Sound '{name}' not loaded. Use load_sound() first.")
            return None

        sound = self.sounds[name]
        if fade_ms > 0:
            return sound.play(loops=loops, maxtime=maxtime, fade_ms=fade_ms)
        else:
            return sound.play(loops=loops, maxtime=maxtime)


    def stop(self, name: str = None):
        """Stop a sound or all sounds."""
        if name:
            if name in self.sounds:
                self.sounds[name].stop()
        else:
            pygame.mixer.stop()


    def set_volume(self, volume: float):
        """Set the volume for all sounds (0.0 to 1.0)."""
        self.volume = max(0.0, min(1.0, volume))
        for sound in self.sounds.values():
            sound.set_volume(self.volume)


    def get_volume(self) -> float:
        """Get the current volume."""
        return self.volume


    def unload_sound(self, name: str):
        """Unload a sound from cache."""
        if name in self.sounds:
            del self.sounds[name]


    def clear_all(self):
        """Clear all loaded sounds."""
        pygame.mixer.stop()
        self.sounds.clear()

    
    # Convenience methods for specific sounds
    def play_hit_rock(self, loops: int = 0, fade_ms: int = 0):
        """Play the rock hit sound."""
        return self.play('hit_rock', loops=loops, fade_ms=fade_ms)
