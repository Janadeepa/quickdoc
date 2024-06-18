# src/versioning.py

class VersionManager:
    def __init__(self):
        self.versions = {}
        self.current_version = None

    def create_version(self, version_name):
        if version_name in self.versions:
            raise ValueError(f"Version '{version_name}' already exists.")
        self.versions[version_name] = []
        self.current_version = version_name

    def add_change(self, change_description):
        if self.current_version is None:
            raise ValueError("No version selected. Create a version first.")
        self.versions[self.current_version].append(change_description)

    def get_versions(self):
        return list(self.versions.keys())

    def get_changes_for_version(self, version_name):
        if version_name not in self.versions:
            raise ValueError(f"Version '{version_name}' does not exist.")
        return self.versions[version_name]

    def rollback_to_version(self, version_name):
        if version_name not in self.versions:
            raise ValueError(f"Version '{version_name}' does not exist.")
        self.current_version = version_name

# Example usage:
if __name__ == "__main__":
    version_manager = VersionManager()
    version_manager.create_version("1.0.0")
    version_manager.add_change("Initial version created.")
    version_manager.create_version("1.1.0")
    version_manager.add_change("Added support for Python.")
    print(version_manager.get_versions())
    print(version_manager.get_changes_for_version("1.1.0"))
