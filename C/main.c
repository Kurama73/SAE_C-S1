/**
 * \file     main.c
 * \brief
 * \author   Tom FRUMY
 * \version  0.1
 * \date     19/12/23
 */


#include "main.h"

// Fonction principale
int main()
{
    // D�claration d'un tableau de structures de type Vol
    struct Vol tableau_vols[MAX_FLIGHTS];
    int nombre_vols = 0;
    int nombre_passagers = 0;

    // Charger les donn�es � partir du CSV
    structure(tableau_vols, &nombre_vols);

    // Afficher le menu
    menu(tableau_vols, nombre_vols, nombre_passagers);

    return 0;
}
