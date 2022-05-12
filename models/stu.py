from tortoise import Model, fields


class Students(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50)

    def __str__(self):
        return f"Student {self.id}: {self.name}"
