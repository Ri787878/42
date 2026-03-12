#include "push_swap.h"

static void ps_init(t_ps_struct *ps)
{
    ps->cmds = NULL;
    ps->ac = 0;
    ps->av = NULL;
    ps->cmd_count = 0;
    ps->temp_node = NULL;
    ps->a = NULL;
    ps->b = NULL;
}

static t_list *make_node(int val)
{
    int *p;

    p = (int *)malloc(sizeof(int));
    if (!p)
        return (NULL);
    *p = val;
    return (ft_lstnew(p));
}

static void add_values(t_list **lst, int *vals, int len)
{
    int i;

    i = 0;
    while (i < len)
    {
        ft_lstadd_back(lst, make_node(vals[i]));
        i++;
    }
}

static void print_content(void *content)
{
    ft_printf("%d ", *(int *)content);
}

static void print_stacks(t_ps_struct *ps)
{
    ft_printf("stack A:\t");
    ft_lstiter(ps->a, print_content);
    ft_printf("\nstack B:\t");
    ft_lstiter(ps->b, print_content);
    ft_printf("\n");
}

static void test_pb_demo(void)
{
    t_ps_struct ps;
    int av[] = {3, -5, 1, 7, -2, -8, 4, -1, 6, -6, 0, 5, -3, 2, -7, -4};

    ps_init(&ps);
    add_values(&ps.a, av, 16);
    print_stacks(&ps);
    pb(&ps);
    print_stacks(&ps);
    ft_lstclear(&ps.a, free);
    ft_lstclear(&ps.b, free);
}

static void test_all_moves_demo(void)
{
    t_ps_struct ps;
    int av[] = {1, 2, 3};
    int bv[] = {4, 5, 6};

    ps_init(&ps);
    add_values(&ps.a, av, 3);
    add_values(&ps.b, bv, 3);
    ft_printf("=== move demo ===\n");
    print_stacks(&ps);
    sa(&ps);
    sb(&ps);
    ss(&ps);
    pb(&ps);
    pa(&ps);
    print_stacks(&ps);
    ft_lstclear(&ps.a, free);
    ft_lstclear(&ps.b, free);
}

int main(void)
{
    test_pb_demo();
    test_all_moves_demo();
    return (0);
}
