<?phpdefined('BASEPATH') OR exit('no direct script access allowed');


class menu extends CI_controller {
    public function index()
    {
        $data = array(
            'content'=> 'dasboard/index.php'
        );
        $this->load->view('template/menu');
    }
}