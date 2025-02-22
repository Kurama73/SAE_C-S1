/**
 * \file     main.c
 * \brief
 * \author   Tom FRUMY et Timoth�e RAZAFINDRANARY et Enzo SACCONE
 * \version  0.1
 * \date     19/12/23
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Dclaration des constantes et structures
#define MAX_FLIGHTS 100
#define MAX_PASSENGERS_PER_FLIGHT 100
#define VINGT 20
#define ONZE 11
#define CINQUANTE 50
#define CENT 100
#define MILLE 1000
#define SIX_CENT 600
#define TRENTE 30
#define DEUX_MILLE_DEUX_CENT 2200
#define CINQ 5
#define TROIS_CENT 300
#define DEUX 2
#define DOUZE 12
#define DEUX_MILLE_VINGT_QUATRE 2024


// Structure reprsentant un passager
struct Passager
{
    char nom[CINQUANTE];
    char prenom[CINQUANTE];
    int jour_naissance;
    int mois_naissance;
    int annee_naissance;
    int numero_siege;
    float prix_billet;
};

// Structure reprsentant un vol
struct Vol
{
    int numero_vol;
    char compagnie[CINQUANTE];
    char destination[CINQUANTE];
    int numero_comptoir;
    int heure_debut_enregistrement;
    int heure_fin_enregistrement;
    int salle_embarquement;
    int heure_debut_embarquement;
    int heure_fin_embarquement;
    int heure_decollage;
    char etat_vol[VINGT];
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
void tri_prix (struct Passager tableau_passagers[], const int nombre_passagers);
void opti(struct Vol tableau_vols[], int nombre_vols);
void afficherCompagnieDestination(struct Vol tableau_vols[], int nombre_vols);

