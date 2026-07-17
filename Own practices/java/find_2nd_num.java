public class find_2nd_num {

    public static int secondLargest(int[] arr) {

        if (arr.length < 2)
            return -1;

        int largest = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;

        for (int num : arr) {

            if (num > largest) {
                second = largest;
                largest = num;
            } else if (num > second && num != largest) {
                second = num;
            }
        }

        if (second == Integer.MIN_VALUE)
            return -1;

        return second;
    }

    public static void main(String[] args) {

        int[] arr = {10, 20, 5, 20, 8, 18, 15};

        System.out.println(secondLargest(arr));
    }
}