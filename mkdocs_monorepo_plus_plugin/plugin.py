# Copyright 2023 Deepworks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import yaml
import shutil

from mkdocs_monorepo_plugin.plugin import MonorepoPlugin
from mkdocs.config import config_options
from mkdocs import utils

class MonorepoPlusPlugin(MonorepoPlugin):

    # Add custom options
    config_scheme = (
        ('merged_docs_dir', config_options.Type(str, default='')),
    )

    # Constructor
    def __init__(self):
        # Run the parent constructor
        super().__init__()
        self.merged_docs_dir = None

    # On Config
    def on_config(self, config, **kwargs):

        # Run the parent configuration method
        super().on_config(config)

        # If no 'nav' defined, we don't need to run.
        if not config.get('nav'):
            return config
        
        # Pull in custom configuration options
        default_config = dict((name, config_option.default)
                              for name, config_option in self.config_scheme)
        
        # Add to the configuration
        config['mkdocs_monorepo_plus_config'] = yaml.dump(
            default_config,
            sort_keys=False,
            default_flow_style=False,
            allow_unicode=True,
            encoding=None)
        
        # If no 'merged_docs_dir' defined, we don't need to run.
        if not self.config['merged_docs_dir']:
            return config
           
        self.create_merged_docs(config)

        return config
    
    def create_merged_docs(self, config):

        # Grab original configuration file path
        with open(config.get('config_file_path'), 'r') as file:
            original_config = yaml.safe_load(file)

        # Check for docs_dir in the original config file
        if not original_config.get('docs_dir'):
            original_config['docs_dir'] = "docs"
           
        # Set the 'docs' directory under the merged_docs_dir
        self.config['merged_docs_dir_src'] = self.config['merged_docs_dir']+os.sep+original_config['docs_dir']

        # Clean the directory first
        if os.path.exists(self.config['merged_docs_dir_src']) and os.path.isdir(self.config['merged_docs_dir_src']):
            shutil.rmtree(self.config['merged_docs_dir_src'])

        # Copy the files created by monorepo to the merged docs dir
        shutil.copytree(config['docs_dir'], self.config['merged_docs_dir_src'])

        # Log this
        utils.log.info(
            "mkdocs-monorepo-plus-plugin: merged_docs_dir: %s",
            self.config['merged_docs_dir_src'])
        
        # Update our nav with what monorepo created
        original_config['nav'] = config['nav']

        # Remove the plugin for the new config as we don't need it anymore
        plugins = original_config.get('plugins')
        for p in plugins:
            if p.get('monorepoplus'):
                plugins.remove(p)
                original_config['plugins'] = plugins

        # Create our new merged config file
        with open(self.config['merged_docs_dir']+os.sep+'mkdocs.yml', 'w') as file:
            yaml.safe_dump(original_config, file)