#pragma once

typedef int TElem;

#define NULL_TELEMENT 0
#define INITIAL_SIZE 2
#define INVALID_INDEX (-1)

class Matrice {

private:
    /* aici e reprezentarea */
    struct matrixElement{
        int line, column;
        TElem valoare;
    };

    // define a comparison function for matrix elements
    static int functieComparare(const matrixElement& firstElement, const matrixElement& secondElement) ;

    // define a node structure to be stored in the array
    struct Node{
        matrixElement info;
        int left, right;
    };

    struct BinarySearchTree{
        int root;
        Node* elements;
        int size, capacity, indexFirstEmpty;
    };

    int search(int linie, int coloana) const;
    int insertNodeRecursive(int headIndex, matrixElement toBeAdded);
    //int removeRecursively(int headIndex, matrixElement toBeRemoved);
    //int minimumElementIndex(int currentNode);
    void addNode(int i, int j, TElem e);
    //void removeNode(int i, int j);
    void resize();

private:

    int lines, columns;
    BinarySearchTree BST{};


public:

    //constructor
    //se arunca exceptie daca nrLinii<=0 sau nrColoane<=0
    Matrice(int nrLinii, int nrColoane);


    //destructor
    ~Matrice();

    //returnare element de pe o linie si o coloana
    //se arunca exceptie daca (i,j) nu e pozitie valida in Matrice
    //indicii se considera incepand de la 0
    TElem element(int i, int j) const;


    // returnare numar linii
    int nrLinii() const;

    // returnare numar coloane
    int nrColoane() const;


    // modificare element de pe o linie si o coloana si returnarea vechii valori
    // se arunca exceptie daca (i,j) nu e o pozitie valida in Matrice
    TElem modifica(int i, int j, TElem);

};






