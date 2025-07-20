def run_collectors(config):
    all_data = []

    if "github" in config["collector"]["sources"]:
        from .sources.github import collect_github
        all_data.extend(collect_github(config))

    if "reddit" in config["collector"]["sources"]:
        from .sources.reddit import collect_reddit
        all_data.extend(collect_reddit(config))

    if "dark_web" in config["collector"]["sources"]:
        from .sources.darkweb import collect_darkweb
        all_data.extend(collect_darkweb(config))

    return all_data
