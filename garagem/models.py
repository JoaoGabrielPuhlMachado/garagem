from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome.upper()


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Cor(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "cores"


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="veiculos")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="veiculos")
    ano = models.IntegerField(null=True, blank=True)
    preco = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, null=True, blank=True
    )
    descricao = models.CharField(max_length=50, null=True, blank=True)
    acessorio = models.ManyToManyField(Acessorio, related_name="veiculos")

    def __str__(self):
        return f"{self.marca} {self.categoria} {self.ano} ({self.cor})"

    class Meta:
        verbose_name_plural = "veículos"
