import unittest
from unittest.mock import MagicMock, patch
import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

# Add the parent directory to sys.path to import the main module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from god_is_saying_lol.__main__ import VideoPlayer, resource_path, onDeath, onGameJoin, onRespawn

class TestVideoPlayer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create QApplication instance for tests
        cls.app = QApplication([])

    def setUp(self):
        # Create a mock video path for testing
        self.video_path = "test_video.mp4"
        self.player = VideoPlayer(self.video_path)

    def test_init(self):
        """Test VideoPlayer initialization"""
        self.assertEqual(self.player.video_path, self.video_path)
        self.assertEqual(self.player.windowFlags() & Qt.FramelessWindowHint, Qt.FramelessWindowHint)
        self.assertEqual(self.player.windowFlags() & Qt.WindowStaysOnTopHint, Qt.WindowStaysOnTopHint)
        self.assertEqual(self.player.windowOpacity(), 0.7)

    def test_media_player_settings(self):
        """Test media player initial settings"""
        self.assertEqual(self.player.media_player.volume(), 25)

    @patch('PyQt5.QtMultimedia.QMediaPlayer.stop')
    def test_escape_key_press(self, mock_stop):
        """Test escape key press event"""
        # Create a mock key event for Escape key
        event = MagicMock()
        event.key.return_value = Qt.Key_Escape
        
        self.player.keyPressEvent(event)
        mock_stop.assert_called_once()

class TestResourcePath(unittest.TestCase):
    def test_resource_path_normal(self):
        """Test resource_path function with normal path"""
        test_path = "test/path"
        result = resource_path(test_path)
        self.assertTrue(os.path.isabs(result))
        self.assertTrue(test_path in result)

    @patch('sys._MEIPASS', new='mocked_meipass')
    def test_resource_path_meipass(self):
        """Test resource_path function with PyInstaller _MEIPASS"""
        test_path = "test/path"
        result = resource_path(test_path)
        self.assertTrue('mocked_meipass' in result)
        self.assertTrue(test_path in result)

class TestEventHandlers(unittest.TestCase):
    @patch('god_is_saying_lol.__main__.VideoPlayer')
    @patch('os.path.exists')
    def test_on_death(self, mock_exists, mock_video_player):
        """Test onDeath event handler"""
        mock_exists.return_value = True
        mock_instance = MagicMock()
        mock_video_player.return_value = mock_instance

        # Patch QApplication to prevent actual GUI creation
        with patch('PyQt5.QtWidgets.QApplication'):
            onDeath()
            mock_exists.assert_called_once()
            mock_video_player.assert_called_once()
            mock_instance.show.assert_called_once()

    @patch('god_is_saying_lol.__main__.VideoPlayer')
    @patch('os.path.exists')
    def test_on_game_join(self, mock_exists, mock_video_player):
        """Test onGameJoin event handler"""
        mock_exists.return_value = True
        mock_instance = MagicMock()
        mock_video_player.return_value = mock_instance

        with patch('PyQt5.QtWidgets.QApplication'):
            onGameJoin()
            mock_exists.assert_called_once()
            mock_video_player.assert_called_once()
            mock_instance.show.assert_called_once()

    @patch('god_is_saying_lol.__main__.VideoPlayer')
    @patch('os.path.exists')
    def test_on_respawn(self, mock_exists, mock_video_player):
        """Test onRespawn event handler"""
        mock_exists.return_value = True
        mock_instance = MagicMock()
        mock_video_player.return_value = mock_instance

        with patch('PyQt5.QtWidgets.QApplication'):
            onRespawn()
            mock_exists.assert_called_once()
            mock_video_player.assert_called_once()
            mock_instance.show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
