/**
 * \file     main.c
 * \brief
 * \author   Tom FRUMY
 * \version  0.1
 * \date     19/12/23
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Déclaration des constantes et structures
#define MAX_FLIGHTS 100
#define MAX_PASSENGERS_PER_FLIGHT 100

// Structure représentant un passager
struct Passager
{
    char nom[50];
    char prenom[50];
    char date_naissance[11];
    int numero_siege;
    float prix_billet;
};

// Structure représentant un vol
struct Vol
{
    int numero_vol;
    char compagnie[50];
    char destination[50];
    int numero_comptoir;
    int heure_debut_enregistrement;
    int heure_fin_enregistrement;
    int salle_embarquement;
    int heure_debut_embarquement;
    int heure_fin_embarquement;
    int heure_decollage;
    char etat_vol[20];
    int nombre_passagers;
    struct Passager passagers[MAX_PASSENGERS_PER_FLIGHT];
};

// Prototypes des fonctions
void structure(struct Vol tableau_vols[], int *nombre_vols);
void menu(struct Vol tableau_vols[], int nombre_vols, int nombre_passagers);
void tableau_information(struct Vol tableau_vols[], int nombre_vols);
void afficherPassagers(struct Vol tableau_vols[], int numero_vol);
void afficherVolHeure(struct Vol tableau_vols[], int heure, int nombre_vols);
void afficherDestination(struct Vol tableau_vols[], int nombre_vols);
void afficherCompagnie(struct Vol tableau_vols[], int nombre_vols);
void trieprix (struct Vol tableau_vols[],int numero_vol);
void trieage(struct Vol tableau_vols[], int numero_vol);
void trienom(struct Vol tableau_vols[], int numero_vol);
