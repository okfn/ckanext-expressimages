import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class CkanExpressImagesPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    def update_config(self, config):
        toolkit.add_public_directory(config, "public")
