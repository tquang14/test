package BAI1;

class hcn {
    private float d, r;
    protected void set(float d, float r) {
        this.d = d;
        this.r = r;
    }
    protected void show() {
        System.out.println("chieu dai: " + this.d);
        System.out.println("chieu rong: " + this.r);
    }
    protected float dienTich(float d, float r) {
        return d * r;
    }
    protected float chuVi(float d, float r) {
        return (d + r) / 2;
    }
    protected static void showKetQua(float dt, float cv) {
        System.out.println("dien tich: " + dt);
        System.out.println("chu vi: " + cv);
    }
}

public class BAI1 {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello Java");
        hcn A = new hcn();
        A.set(5, 4);
        A.show();
        hcn.showKetQua(A.dienTich(5, 4), A.chuVi(5, 4));
    }
}