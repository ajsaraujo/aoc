#include <stdio.h>
#include <stdlib.h>

int max(int a, int b) {
	if (a > b) {
		return a;
	}

	return b;
}

int min(int a, int b) {
    if (a < b) {
       return a;
    }

    return b;
}

int power(int base, int expoent) {
	if (expoent == 1) {
		return base;
	}

	return base * power(base, expoent - 1);
}

int binary_search(char left_command, char right_command, int num_of_commands, char * commands) {
	int num_of_options = power(2, num_of_commands);

	int left = 0;
	int right = right = num_of_options - 1;
	int mid = (left + right) / 2;

	printf("s = %s\n", commands);

	for (int i = 0; i < num_of_commands - 1; i++) {
		if (commands[i] == left_command) {
			right = mid;
		} else {
			left = mid + 1;
		}

		mid = (left + right) / 2;
		printf("l = %d, m = %d, r = %d\n", left, mid, right);
	}

	if (commands[num_of_commands - 1] == left_command) {
		return left;
	}

	return right;
}

int calculate_seat_id(char * seat) {
	int row = binary_search('F', 'B', 7, seat);
	int column = binary_search('L', 'R', 3, seat + 7);

	printf("Row = %d\n", row);
	printf("Column = %d\n", column);

	return (row * 8) + column;
}

char seats[1000][15];
int num_of_seats;
int biggest_seat_id;
int smallest_seat_id;
int * seat_ids;
int * seat_is_taken;

int main() {
	while (scanf("%s", seats[num_of_seats]) != EOF) {
		num_of_seats++;
	}

	seat_ids = malloc(sizeof(int) * num_of_seats);
	smallest_seat_id = 1100;

	for (int i = 0; i < num_of_seats; i++) {
		seat_ids[i] = calculate_seat_id(seats[i]);
		biggest_seat_id = max(biggest_seat_id, seat_ids[i]);
	        smallest_seat_id = min(smallest_seat_id, seat_ids[i]);
	}

	seat_is_taken = calloc(biggest_seat_id + 1, sizeof(int));

	for (int i = 0; i < num_of_seats; i++) {
		int seat_id = seat_ids[i];
	        seat_is_taken[seat_id] = 1;
	}

	for (int i = smallest_seat_id; i <= biggest_seat_id; i++) {
		if (!seat_is_taken[i]) {
			printf("Seat %d is not taken\n", i)
        	}
	}

	return 0;
}
