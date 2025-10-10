class BaseRepository:
    def __init__(self, queryset=None) -> None:
        """Init with a custom queryset"""
        self.base_queryset = queryset

    def __len__(self):
        return self.base_queryset.count()

    def __iter__(self):
        for task in self.base_queryset:
            yield task

    def __contains__(self, key):
        return self.base_queryset.filter(id=key).exists()

    def __getitem__(self, key):
        try:
            return self.base_queryset.get(id=key)
        except self.base_queryset.model.DoesNotExist:
            raise KeyError("Task not found")

    def insert(self, item):
        item.save()
