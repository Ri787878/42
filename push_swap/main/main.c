/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/13 11:45:14 by ridias            #+#    #+#             */
/*   Updated: 2026/02/13 13:00:40 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

typedef	struct	Node
{
	int	data;
	struct	Node	*next;
	struct	Node	*prev;
}	Node;

Node	*createNode(int data)
{
	Node	*newNode = (Node *)malloc(sizeof(Node));

	newNode->data = data;
	newNode->next = NULL;
	newNode->prev = NULL;
	return newNode;
}

Node	*addstart(Node **head, int data)
{
	Node	*newNode;
	
	newNode = createNode(data);
	if (*head == NULL)
	{
		*head = newNode;
		return;
	}
	newNode->next = *head;
	(*head)->prev = newNode;
	*head = newNode;
}

Node	*add_end(Node **head, int data)
{
	Node	*newNode;
	Node	*temp;
	
	newNode = createNode(data);
	temp = *head;
	if(*head == NULL)
	{
		*head = newNode;
		//add free of the temp node
		return;
	}
	while (temp->next != NULL)
	{
		temp = temp->next;
	}
	temp->next = newNode;
	newNode->prev = temp;
}

Node *addmiddle(Node **head, int data, int position)
{
	Node	*newNode;
	Node	*temp;
	int		i;

	//Error if position is the head 
	if (position < 1)
		return;
	if (position == 1)
	{
		addstart(head, data);
		//free newNode and temp
		return;
	}
	newNode = createNode(data);
	temp = *head;
	i = 0;
	while (temp != NULL && i < position - 1)
	{
		temp = temp->next;
		i++;
	}
	//Error if position is bigger than number of nodes.
	if(temp == NULL)
		return;
	newNode->next = temp->next;
	newNode->prev = temp;
	//Need to review this if it is weird
	if (temp->next != NULL)
		temp->next->prev = newNode;
	temp->next = newNode;
}