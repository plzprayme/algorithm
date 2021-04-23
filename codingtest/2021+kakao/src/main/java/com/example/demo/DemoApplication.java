package com.example.demo;

import java.util.HashMap;

public class DemoApplication {

	public static void main(String[] args) {
		System.out.println(solution1());

		

	}

	private static int solution1() {
		HashMap<Integer, Integer> gift_counter = new HashMap<Integer, Integer>();
		HashMap<Integer, Integer> wants_counter = new HashMap<Integer, Integer>();

		// int[] gift_cards = {4,5,3,2,1};
		// int[] wants = {2,4,4,5,1};

		int[] gift_cards = {5,4,5,4,5};
		int[] wants = {1,2,3,5,4};

		for (int i =0; i < gift_cards.length; i++) {
			if (gift_counter.containsKey((gift_cards[i]))) {
				gift_counter.put(gift_cards[i], gift_counter.get(gift_cards[i]) + 1);
			} else {
				gift_counter.put(gift_cards[i], 1);
			}

			if (wants_counter.containsKey((wants[i]))) {
				System.out.println("key: ");
				wants_counter.put(wants[i], wants_counter.get(wants[i]) + 1);
			} else {
				wants_counter.put(wants[i], 1);
			}
		}

		System.out.println(gift_counter.toString());
		System.out.println(wants_counter.toString());

		int answer = 0;
		for (int i : wants_counter.keySet()) {
			System.out.println("key: " + i);
			System.out.println(wants_counter.get(i));
			try {
				int num = wants_counter.get(i) - gift_counter.get(i);
				if (num > 0) {
					answer += num;
				}
			} catch (Exception e) {
				answer += wants_counter.get(i);
			}

		}

		return answer;
	}

}
