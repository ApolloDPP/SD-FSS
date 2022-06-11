import nibabel as nib
import cv2

def nii_read(path):
    raw=nib.load(path)
    affine=raw.affine
    data=raw.get_data()
    return data,affine


if __name__=='__main__':

    path = 'D:\\FSL\\data\\FLARE2021\\TrainingImg\\train_000_0000.nii.gz'
    data,affine=nii_read(path)
    print(6666)




# new_image = nib.Nifti1Image(lab_data, lab_affine)
# nib.save(new_image,  "D:\\KIT21\\slight\\test\\soft_lab\\S"+path.split("\\")[-1])



