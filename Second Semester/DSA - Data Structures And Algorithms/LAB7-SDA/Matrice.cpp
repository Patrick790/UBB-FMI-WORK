#include "Matrice.h"

#include <exception>

using namespace std;

// tetha(1)
Matrice::Matrice(int nrLinii, int nrColoane) {
    /* de adaugat */
    this->lines = nrLinii;
    this->columns = nrColoane;
    // initially the root is at an invalid index
    this->BST.root = INVALID_INDEX;
    // the size is 0
    this->BST.size = 0;
    // index first empty is also zero
    this->BST.indexFirstEmpty = 0;
    // capacity is equal the predefined value
    this->BST.capacity = INITIAL_SIZE;
    // create a vector of Nodes of size capacity
    this->BST.elements = new Node[this->BST.capacity];
}

// tetha(1)
int Matrice::nrLinii() const{
    /* de adaugat */
    return this->lines;
}

// tetha(1)
int Matrice::nrColoane() const{
    /* de adaugat */
    return this->columns;
}

// O(size)
// return the value of the element at position [i,j] in the matrix if it exists, NULL_TELEM otherwise.
TElem Matrice::element(int i, int j) const{
    /* de adaugat */
    if(i < 0 || i > this->nrLinii() || j < 0 || j > this->nrColoane())
        throw std::exception();
    auto node = this->search(i, j);
    if(node != INVALID_INDEX)
        return this->BST.elements[node].info.valoare;
    return NULL_TELEMENT;
}

// O(size)
TElem Matrice::modifica(int i, int j, TElem e) {
    /* de adaugat */
    if(i < 0 || i > this->nrLinii() || j < 0 || j > this->nrColoane())
        throw std::exception();
    auto node = this->search(i,j);
    //we have 4 cases:
    // case 1: node exists, e.value != null_telem -> update its value
    // case 2: node exists, e.value  = null_telem -> delete the node
    // case 3: node does not exist, e.value != null_telem -> add the node
    // case 4: node does not exist, e.value = null_telem -> do nothing
    if(node != INVALID_INDEX)
    {
        //save its old value
        TElem savedValue = this->BST.elements[node].info.valoare;
        //set its new value
        this->BST.elements[node].info.valoare = e;
        return savedValue;
    } else if (e != NULL_TELEMENT){
        this->addNode(i,j,e);
    }

    return NULL_TELEMENT;
}

// returns -1 if firstElement < secondElement, 0 if firstElement = secondElement, 1 if firstElement > secondElement
// tetha(1)
int Matrice::functieComparare(const Matrice::matrixElement &firstElement,
                              const Matrice::matrixElement &secondElement) {
    int aux;
    aux = firstElement.line - secondElement.line;
    if(aux < 0)
        return -1;
    else if(aux > 0)
        return 1;
    else {
        aux = firstElement.column - secondElement.column;
        if(aux < 0)
            return -1;
        else if(aux > 0)
            return 1;
        else return 0;
    }
}

// O(size)
int Matrice::search(int linie, int coloana) const {
    if(linie < 0 || coloana < 0 || linie >this->lines || coloana > this->columns)
        return INVALID_INDEX;
    // create a searchedElement to search for
    matrixElement searchedElement{};
    searchedElement.line = linie;
    searchedElement.column = coloana;
    // start the search from the root
    auto currentNode = this->BST.root;
    while(currentNode != INVALID_INDEX) {
        // we found the element
        if (this->functieComparare(this->BST.elements[currentNode].info, searchedElement) == 0)
            return currentNode;
            // if the element we are looking for is greater than the current element. search in the right subtree
        else if(this->functieComparare(this->BST.elements[currentNode].info, searchedElement) < 0)
            currentNode = this->BST.elements[currentNode].right;
            // otherwise search in the left subtree
        else
            currentNode = this-> BST.elements[currentNode].left;
    }
    //element not found
    return INVALID_INDEX;

}

// O(size)
int Matrice::insertNodeRecursive(int headIndex, matrixElement value) {
    if(headIndex == INVALID_INDEX)
    {
        // set index to be inserted to first empty
        int indexToBeInserted = this->BST.indexFirstEmpty;
        // move first empty to next empty
        this->BST.elements[indexToBeInserted].right = INVALID_INDEX;
        this->BST.elements[indexToBeInserted].left = INVALID_INDEX;
        this->BST.elements[indexToBeInserted].info = value;
        this->BST.size++;
        this->BST.indexFirstEmpty++;
        return indexToBeInserted;
    }
    else if(this->functieComparare(this->BST.elements[headIndex].info, value) < 0)
        this->BST.elements[headIndex].right = this->insertNodeRecursive(this->BST.elements[headIndex].right, value);
    else
        this->BST.elements[headIndex].left = this->insertNodeRecursive(this->BST.elements[headIndex].left, value);
    return headIndex;
}

// O(size)
void Matrice::addNode(int i, int j, TElem e) {
    // if the bst is full, resize
    if(this->BST.size == this->BST.capacity)
        this->resize();
    //create the element to be added
    matrixElement elementToBeAdded;
    elementToBeAdded.line = i;
    elementToBeAdded.column = j;
    elementToBeAdded.valoare = e;
    //case 1: the root is empty
    if(this->BST.root == INVALID_INDEX)
    {
        this->BST.root = 0;
        this->BST.elements[0].left = INVALID_INDEX;
        this->BST.elements[0].right = INVALID_INDEX;
        this->BST.elements[0].info = elementToBeAdded;
        this->BST.size++;
        this->BST.indexFirstEmpty++;
        return ;
    }
    //case 2: non-empty tree
    this->insertNodeRecursive(this->BST.root, elementToBeAdded);
}

// O(size)
void Matrice::resize() {
    int newCapacity = this->BST.capacity * 2;
    Node* newElements = new Node[newCapacity];
    for(int i=0; i < this->BST.size; i++)
        newElements[i] = this->BST.elements[i];
    delete[] this->BST.elements;
    this->BST.elements = newElements;
    this->BST.capacity = newCapacity;
}



Matrice::~Matrice() {
    delete[] this->BST.elements;
}



