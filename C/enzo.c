/**
 * \file     enzo.c
 * \brief
 * \author   Enzo Saccone
 * \version  0.1
 * \date     19/12/23
 */


#include "main.h"

void panneau_passagerp(struct Vol tableau_vols[], int nombre_vols)
{
    tri_prix(tableau_vols, nombre_vols);
    //age(tableau_vols, tableau_vols[*nombre_vols].passagers[i].date_naissance);
    afficherPassagers_entete(tableau_vols, nombre_vols);
    afficherPassagers(tableau_vols, nombre_vols);
}

/*int age(tableau_vols,date_naissance)
{
    //calucule age
    age=2024-date_naissance
}
*/























void panneau_passagera(struct Vol tableau_vols[], int numero_vol)
{
    trieage(tableau_vols, numero_vol);
    afficherPassagers_entete(tableau_vols, numero_vol);
    afficherPassagers(tableau_vols, numero_vol);
}

void panneau_passagern(struct Vol tableau_vols[], int numero_vol)
{
    trienom(tableau_vols, numero_vol);
    afficherPassagers_entete(tableau_vols, numero_vol);
    afficherPassagers(tableau_vols, numero_vol);
}


