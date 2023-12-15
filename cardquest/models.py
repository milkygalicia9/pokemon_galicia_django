from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Trainer(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class PokemonCard(BaseModel):
    RARITY_CHOICES = (
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
    )

    CARDTYPE_CHOICES = (
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Grass', 'Grass'),
        ('Electric', 'Electric'),
        ('Psychic', 'Psychic'),
        ('Ice', 'Ice'),
        ('Dragon', 'Dragon'),
        ('Dark', 'Dark'),
        ('Normal', 'Normal'),
        ('Fighting', 'Fighting'),
        ('Flying', 'Flying'),
        ('Poison', 'Poison'),
        ('Ground', 'Ground'),
        ('Rock', 'Rock'),
        ('Bug', 'Bug'),
        ('Ghost', 'Ghost'),
        ('Steel', 'Steel'),
        ('Fairy', 'Fairy'),
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    rarity = models.CharField(max_length=100, choices=RARITY_CHOICES, null=True, blank=True)
    hp = models.IntegerField(null=True, blank=True)
    card_type = models.CharField(max_length=100, choices=CARDTYPE_CHOICES, null=True, blank=True)
    attack = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    weakness = models.CharField(max_length=250, null=True, blank=True)
    card_number = models.IntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    evolution_stage = models.CharField(max_length=250, null=True, blank=True)
    abilities = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Collection(BaseModel):
    card = models.ForeignKey(PokemonCard, on_delete=models.CASCADE, null=True, blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    collection_date = models.DateField()

    def __str__(self):
        return self.trainer.name + " - " + self.card.name
