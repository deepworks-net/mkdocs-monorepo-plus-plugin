import setuptools

# Setup the plugin
setuptools.setup(
    name='mkdocs-monorepo-plus-plugin',
    version='1.0.0',
    description='A Plugin for adding and extending the monorepo-plugin with extra options and functionality.',
    long_description="""
       A Plugin for adding and extending the monorepo-plugin with extra options and functionality.
    """,  # noqa: E501
    keywords='mkdocs monorepo monorepoplus monorepo-plus',
    url='https://github.com/deepworks-ny/mkdocs-monorepo-plus-plugin',
    author='Deepworks',
    author_email='support@deepworks.net',
    license='Apache-2.0',
    python_requires='>=3',
    install_requires=[
        'mkdocs>=1.5.2',
        'mkdocs-material>=9.2.8',
        'mkdocs-material-extensions>=1.1.1',
        'mkdocs-macros-plugin>=1.0.2',
        'mkdocs-monorepo-plugin>=1.0.5'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    packages=setuptools.find_packages(),
    entry_points={
        'mkdocs.plugins': [
            "monorepoplus = mkdocs_monorepo_plus_plugin.plugin:MonorepoPlusPlugin"
        ]
    }
)
