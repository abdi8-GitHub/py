#ifndef LISTS_H
#define LISTS_H

typedef strut listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

listint_t *insert_node(listint_t **head, int number);


#endif /* LISTS_H */