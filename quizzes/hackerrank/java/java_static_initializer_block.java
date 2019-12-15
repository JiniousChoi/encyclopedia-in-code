// author: jinchoiseoul@gmail.com

static int B;
static int H;
static boolean flag = true;
static {
    Scanner scan = new Scanner(System.in);
    B = scan.nextInt();
    H = scan.nextInt();
    if (B<=0 || H <=0) {
        flag = false;
        System.out.println("java.lang.Exception: Breadth and height must be positive");
    }
}
