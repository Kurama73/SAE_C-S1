/**
 * \file     afficher_passagers.c
 * \brief
 * \author   Tom FRUMY et Enzo SACCONE
 * \version  0.1
 * \date     19/12/23
 */


#include "main.h"

// Afficher les passagers d'un vol
void afficherPassagers(struct Vol tableau_vols[], int numero_vol) // A modifier par enzo
{

    for (int i = 0; i < tableau_vols[numero_vol - 1].nombre_passagers; i++)
    {


        printf("| %-18s | %-18s | %02d/%02d/%4d | %-5d | %-11.2f |\n",
               tableau_vols[numero_vol - 1].passagers[i].nom,
               tableau_vols[numero_vol - 1].passagers[i].prenom,
               tableau_vols[numero_vol - 1].passagers[i].jour_naissance,
               tableau_vols[numero_vol - 1].passagers[i].mois_naissance,
               tableau_vols[numero_vol - 1].passagers[i].annee_naissance,
               tableau_vols[numero_vol - 1].passagers[i].numero_siege,
               tableau_vols[numero_vol - 1].passagers[i].prix_billet);
    }

    }


void afficherPassagers_entete(int numero_vol)
{
    printf("\nPassagers du vol %d :\n", numero_vol);
    printf("===========================================================\n");
    printf("| Nom                | Prenom             | Date de naissance | Siege | Prix billet |\n");
    printf("===========================================================\n");
}

