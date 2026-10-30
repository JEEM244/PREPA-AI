import json
import tempfile
import unittest
from pathlib import Path
from cli.prepa_ai.config import ConfigError,DEFAULTS,load_config,validate_config

class ConfigTests(unittest.TestCase):
    def test_defaults_load_when_file_missing(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(load_config(Path(folder)/"config.json"),DEFAULTS)
    def test_refuses_network_bind(self):
        config=DEFAULTS.copy(); config["host"]="0.0.0.0"
        with self.assertRaises(ConfigError): validate_config(config)
    def test_refuses_invalid_port(self):
        config=DEFAULTS.copy(); config["port"]=80
        with self.assertRaises(ConfigError): validate_config(config)
    def test_loads_custom_temperature(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/"config.json"
            path.write_text(json.dumps({"temperature":0.2}),encoding="utf-8")
            self.assertEqual(load_config(path)["temperature"],0.2)

if __name__=="__main__": unittest.main()
